/**
 * record.js — Capture GSAP animation frames and encode to MP4
 *
 * Strategy: modify the HTML to use a GSAP tick-based frame exporter
 * (no real-time, deterministic frame-by-frame at 30fps), save PNGs,
 * then stitch with ffmpeg.
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');
const { execSync } = require('child_process');

const FRAMES_DIR = path.join(__dirname, 'frames');
const OUT_MP4    = path.join(__dirname, 'cigarette-journey.mp4');
const FPS        = 30;
const DURATION   = 90; // seconds — full timeline + buffer
const W          = 1280;
const H          = 720;

if (fs.existsSync(FRAMES_DIR)) fs.rmSync(FRAMES_DIR, { recursive: true });
fs.mkdirSync(FRAMES_DIR);

(async () => {
  console.log('Launching browser...');
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-gpu',
      '--disable-dev-shm-usage',
      '--disable-web-security',
    ],
    executablePath: process.env.PUPPETEER_EXEC ||
      '/root/.cache/puppeteer/chrome/linux-149.0.7827.22/chrome-linux64/chrome',
  });

  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });

  const htmlPath = 'file://' + path.join(__dirname, 'record.html');
  console.log('Loading:', htmlPath);
  await page.goto(htmlPath, { waitUntil: 'domcontentloaded', timeout: 30000 });
  page.on('pageerror', e => console.error('Page error:', e.message));

  // Wait for GSAP to be ready
  await new Promise(r => setTimeout(r, 2000));
  await page.waitForFunction(() => typeof gsap !== 'undefined' && typeof window.tl !== 'undefined', { timeout: 15000 });

  // Start the timeline at time 0
  await page.evaluate(() => {
    window.tl.seek(0);
    window.tl.pause();
  });

  const totalFrames = FPS * DURATION;
  console.log(`Capturing ${totalFrames} frames at ${FPS}fps...`);

  for (let f = 0; f < totalFrames; f++) {
    const t = f / FPS;

    await page.evaluate((time) => {
      window.tl.seek(time);
    }, t);

    // Short settle
    await new Promise(r => setTimeout(r, 8));

    const framePath = path.join(FRAMES_DIR, `frame_${String(f).padStart(5, '0')}.png`);
    await page.screenshot({ path: framePath, clip: { x: 0, y: 0, width: W, height: H } });

    if (f % 150 === 0) process.stdout.write(`  Frame ${f}/${totalFrames} (${(t).toFixed(1)}s)\n`);
  }

  await browser.close();
  console.log('All frames captured. Encoding MP4...');

  const ffCmd = [
    'ffmpeg -y',
    `-framerate ${FPS}`,
    `-i "${FRAMES_DIR}/frame_%05d.png"`,
    '-c:v libx264',
    '-preset slow',
    '-crf 18',
    '-pix_fmt yuv420p',
    '-movflags +faststart',
    `"${OUT_MP4}"`
  ].join(' ');

  console.log('Running:', ffCmd);
  execSync(ffCmd, { stdio: 'inherit' });

  console.log('\n✓ Done:', OUT_MP4);
  fs.rmSync(FRAMES_DIR, { recursive: true });
})().catch(err => {
  console.error(err);
  process.exit(1);
});
