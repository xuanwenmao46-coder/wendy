// Captures ai-video-promo-render.html → ai-video-promo.mp4 (30s, 30fps)
const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const FRAME_DIR = '/tmp/promo-frames';
const OUTPUT    = path.resolve(__dirname, 'ai-video-promo.mp4');
const HTML      = `file://${path.resolve(__dirname, 'ai-video-promo-render.html')}`;
const DURATION  = 30;        // seconds to record
const TARGET_MS = 33;        // ~30fps target interval per frame

async function main() {
  if (fs.existsSync(FRAME_DIR)) execSync(`rm -rf ${FRAME_DIR}`);
  fs.mkdirSync(FRAME_DIR, { recursive: true });

  console.log('Launching browser...');
  const browser = await puppeteer.launch({
    headless: true,
    executablePath: process.env.PUPPETEER_EXEC ||
      '/root/.cache/puppeteer/chrome/linux-149.0.7827.22/chrome-linux64/chrome',
    args: [
      '--no-sandbox', '--disable-setuid-sandbox',
      '--disable-dev-shm-usage', '--disable-gpu',
      '--window-size=1280,720',
      '--font-render-hinting=none',
      '--disable-background-timer-throttling',
      '--disable-renderer-backgrounding',
      '--disable-backgrounding-occluded-windows',
    ],
    defaultViewport: { width: 1280, height: 720 }
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });

  console.log('Loading page...');
  await page.goto(HTML, { waitUntil: 'load', timeout: 15000 });

  // Wait for fonts + GSAP to be ready
  await page.waitForFunction(() => window.__READY === true, { timeout: 10000 });
  // Extra settle time for fonts to render
  await new Promise(r => setTimeout(r, 600));

  console.log(`Recording ${DURATION}s @ ~${Math.round(1000/TARGET_MS)}fps...`);

  let frame = 0;
  const start = Date.now();
  const end   = start + DURATION * 1000;

  while (Date.now() < end) {
    const t0  = Date.now();
    const num = String(frame).padStart(5, '0');
    // Force a layout flush so GSAP's rAF-driven style updates are painted
    await page.evaluate(() => document.body.getBoundingClientRect());
    await page.screenshot({
      path: `${FRAME_DIR}/f${num}.jpg`,
      type: 'jpeg',
      quality: 94,
      captureBeyondViewport: false,
    });
    frame++;

    const elapsed = Date.now() - t0;
    const wait    = TARGET_MS - elapsed;
    if (wait > 1) await new Promise(r => setTimeout(r, wait));
  }

  await browser.close();

  const actualFPS = (frame / DURATION).toFixed(1);
  console.log(`Captured ${frame} frames  →  ${actualFPS} fps`);

  // Encode: tell ffmpeg the real capture fps, output at 30fps
  const inFPS = Math.round(frame / DURATION);
  console.log('Encoding with ffmpeg...');
  execSync(
    `ffmpeg -y -framerate ${inFPS} -i ${FRAME_DIR}/f%05d.jpg ` +
    `-vf "fps=30" ` +
    `-c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p ` +
    `${OUTPUT}`,
    { stdio: 'inherit' }
  );

  const size = (fs.statSync(OUTPUT).size / 1024 / 1024).toFixed(1);
  console.log(`\nDone: ${OUTPUT}  (${size} MB)`);
}

main().catch(err => { console.error(err); process.exit(1); });
