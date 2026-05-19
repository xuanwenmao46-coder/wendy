/**
 * render-video.js
 * Renders each Hyperframes beat HTML to frames, then encodes MP4 with ffmpeg.
 * Usage: node render-video.js
 */

const puppeteer = require('puppeteer');
const { spawnSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const FPS = 30;
const WIDTH = 1920;
const HEIGHT = 1080;
const FRAMES_DIR = path.join(__dirname, 'frames');
const OUTPUT = path.join(__dirname, 'preview.mp4');

const VENDOR = path.join(__dirname, 'hyperframes-project', 'vendor');
const GSAP_SRC    = fs.readFileSync(path.join(VENDOR, 'gsap.min.js'), 'utf8');
const ECHARTS_SRC = fs.readFileSync(path.join(VENDOR, 'echarts.min.js'), 'utf8');
const CHARTJS_SRC = fs.readFileSync(path.join(VENDOR, 'chart.umd.js'), 'utf8');

// Beats in order: [htmlFile, timelineKey, duration (seconds)]
const BEATS = [
  ['compositions/beat-1-hook.html',      'beat-1-hook',      4.0],
  ['compositions/beat-2-cliff.html',     'beat-2-cliff',     6.0],
  ['compositions/beat-3-walls.html',     'beat-3-walls',     8.0],
  ['compositions/beat-3b-calendar.html', 'beat-3b-calendar', 8.0],
  ['compositions/beat-4-cost.html',      'beat-4-cost',      6.0],
  ['compositions/beat-4b-pie.html',      'beat-4b-pie',      8.0],
  ['compositions/beat-4c-bar.html',      'beat-4c-bar',      8.0],
  ['compositions/beat-4d-typing.html',   'beat-4d-typing',  10.0],
  ['compositions/beat-5-cta.html',       'beat-5-cta',       4.0],
];

async function renderBeat(browser, beatFile, tlKey, duration, globalFrameOffset) {
  const totalFrames = Math.ceil(duration * FPS);
  const filePath = path.resolve(__dirname, 'hyperframes-project', beatFile);
  const fileUrl = `file://${filePath}`;

  process.stdout.write(`  → ${path.basename(beatFile)} (${totalFrames} frames)…`);

  const page = await browser.newPage();
  await page.setViewport({ width: WIDTH, height: HEIGHT, deviceScaleFactor: 1 });

  // Intercept requests: serve local GSAP for CDN, block everything else external
  await page.setRequestInterception(true);
  page.on('request', req => {
    const url = req.url();
    if (url.startsWith('file://')) {
      req.continue();
    } else if (url.includes('gsap')) {
      req.respond({ status: 200, contentType: 'application/javascript', body: GSAP_SRC });
    } else if (url.includes('echarts')) {
      req.respond({ status: 200, contentType: 'application/javascript', body: ECHARTS_SRC });
    } else if (url.includes('chart') || url.includes('Chart')) {
      req.respond({ status: 200, contentType: 'application/javascript', body: CHARTJS_SRC });
    } else {
      // Block external requests (fonts, etc.) — fallback fonts are fine
      req.abort();
    }
  });

  // Suppress console noise
  page.on('pageerror', () => {});

  await page.goto(fileUrl, { waitUntil: 'domcontentloaded', timeout: 20000 });

  // Give scripts a moment to finish executing (CDN interception can be async)
  await new Promise(r => setTimeout(r, 1500));

  // Confirm GSAP and timeline are ready
  await page.waitForFunction(
    (key) => typeof gsap !== 'undefined' && window.__timelines && !!window.__timelines[key],
    { timeout: 15000, polling: 200 },
    tlKey
  );

  // Freeze GSAP's real-time ticker and setTimeout so we control time deterministically
  await page.evaluate((key) => {
    // Remove gsap from auto-updating
    gsap.ticker.remove(gsap.updateRoot);

    // Freeze setTimeout so typing/interval effects don't fire on their own
    window.setTimeout = () => 0;
    window.clearTimeout = () => {};
    window.setInterval = () => 0;
    window.clearInterval = () => {};
  }, tlKey);

  for (let f = 0; f < totalFrames; f++) {
    const t = f / FPS;

    await page.evaluate((key, seekTime) => {
      const tl = window.__timelines[key];
      // Seek the timeline — suppresses events (2nd arg = false)
      tl.seek(seekTime, false);
      // Force GSAP to push the render
      gsap.updateRoot(seekTime * 1000); // GSAP v3 ticker uses ms
    }, tlKey, t);

    // Yield to allow paint to finish
    await new Promise(r => setImmediate(r));

    const frameIndex = globalFrameOffset + f;
    const framePath = path.join(FRAMES_DIR, `frame_${String(frameIndex).padStart(6, '0')}.png`);
    await page.screenshot({ path: framePath, type: 'png' });

    if ((f + 1) % FPS === 0) process.stdout.write(` ${((f + 1) / FPS).toFixed(0)}s`);
  }

  process.stdout.write(' ✓\n');
  await page.close();
  return totalFrames;
}

async function main() {
  // Prepare frames directory
  if (fs.existsSync(FRAMES_DIR)) {
    fs.rmSync(FRAMES_DIR, { recursive: true });
  }
  fs.mkdirSync(FRAMES_DIR);

  console.log('Launching browser…');
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu',
      '--disable-web-security',
      `--window-size=${WIDTH},${HEIGHT}`,
    ],
  });

  let globalOffset = 0;
  for (const [file, key, duration] of BEATS) {
    const frames = await renderBeat(browser, file, key, duration, globalOffset);
    globalOffset += frames;
  }

  await browser.close();

  console.log(`\nTotal frames: ${globalOffset} (${(globalOffset / FPS).toFixed(1)}s @ ${FPS}fps)`);
  console.log('Encoding MP4…');

  const result = spawnSync('ffmpeg', [
    '-y',
    '-framerate', String(FPS),
    '-i', path.join(FRAMES_DIR, 'frame_%06d.png'),
    '-c:v', 'libx264',
    '-preset', 'fast',
    '-crf', '18',
    '-pix_fmt', 'yuv420p',
    '-movflags', '+faststart',
    OUTPUT,
  ], { stdio: 'inherit' });

  if (result.status !== 0) {
    console.error('ffmpeg failed with exit code', result.status);
    process.exit(1);
  }

  const sizeMB = (fs.statSync(OUTPUT).size / 1024 / 1024).toFixed(1);
  console.log(`\nDone! → ${OUTPUT} (${sizeMB} MB)`);
}

main().catch(err => { console.error(err); process.exit(1); });
