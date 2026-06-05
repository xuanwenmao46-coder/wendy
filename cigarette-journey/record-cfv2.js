const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');
const { execSync } = require('child_process');

const FRAMES_DIR = path.join(__dirname, 'frames_cfv2');
const OUT_MP4    = path.join(__dirname, 'control-failure-v2.mp4');
const FPS        = 30;
const DURATION   = 78;
const W          = 1280;
const H          = 720;

if (fs.existsSync(FRAMES_DIR)) fs.rmSync(FRAMES_DIR, { recursive: true });
fs.mkdirSync(FRAMES_DIR);

(async () => {
  console.log('Launching browser…');
  const browser = await puppeteer.launch({
    headless: true,
    executablePath: '/root/.cache/puppeteer/chrome/linux-149.0.7827.22/chrome-linux64/chrome',
    args: ['--no-sandbox','--disable-setuid-sandbox','--disable-gpu',
           '--disable-dev-shm-usage','--allow-file-access-from-files'],
    protocolTimeout: 300000,
  });

  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });
  page.on('pageerror', e => console.error('Page error:', e.message));

  await page.goto(
    'file://' + path.join(__dirname, 'control-failure-v2.html'),
    { waitUntil: 'domcontentloaded', timeout: 30000 }
  );
  await new Promise(r => setTimeout(r, 2500));

  // Wait for all images to load (fire photos)
  await page.evaluate(() => Promise.all(
    Array.from(document.querySelectorAll('img')).map(img =>
      img.complete ? Promise.resolve() :
      new Promise(res => { img.onload = res; img.onerror = res; })
    )
  ));

  const dur = await page.evaluate(() => window.tl ? window.tl.duration() : -1);
  console.log('Timeline duration:', dur + 's');

  const totalFrames = FPS * DURATION;
  console.log(`Capturing ${totalFrames} frames at ${FPS}fps…`);

  for (let f = 0; f < totalFrames; f++) {
    const t = f / FPS;

    await page.evaluate((time) => { window.tl.seek(time); }, t);

    // Extra settle for word erosion (CH05) and infection grid (CH04)
    const settle = (t >= 28 && t <= 54) ? 18 : 8;
    await new Promise(r => setTimeout(r, settle));

    const fp = path.join(FRAMES_DIR, `f_${String(f).padStart(5,'0')}.png`);
    await page.screenshot({ path: fp, clip: { x:0, y:0, width:W, height:H } });

    if (f % 150 === 0) process.stdout.write(`  ${f}/${totalFrames} (${t.toFixed(1)}s)\n`);
  }

  await browser.close();
  console.log('\nAll frames captured. Encoding MP4…');

  execSync([
    'ffmpeg -y',
    `-framerate ${FPS}`,
    `-i "${FRAMES_DIR}/f_%05d.png"`,
    '-c:v libx264 -preset slow -crf 15 -pix_fmt yuv420p -movflags +faststart',
    `"${OUT_MP4}"`
  ].join(' '), { stdio: 'inherit' });

  console.log('\n✓ Video done:', OUT_MP4);
  fs.rmSync(FRAMES_DIR, { recursive: true });

  // Merge audio if available
  const AUDIO = path.join(__dirname, 'audio-cf.wav');
  const FINAL = OUT_MP4.replace('.mp4', '-final.mp4');
  if (fs.existsSync(AUDIO)) {
    console.log('Merging audio…');
    execSync([
      'ffmpeg -y',
      `-i "${OUT_MP4}"`,
      `-i "${AUDIO}"`,
      '-c:v copy -c:a aac -b:a 192k -shortest',
      `"${FINAL}"`
    ].join(' '), { stdio: 'inherit' });
    console.log('✓ Final with audio:', FINAL);
  }
})().catch(e => { console.error(e); process.exit(1); });
