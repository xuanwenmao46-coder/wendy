// Captures promo-v2.html → promo-v2.mp4
const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const FRAME_DIR = '/tmp/promo-v2-frames';
const OUTPUT    = path.resolve(__dirname, 'promo-v2.mp4');
const HTML      = `file://${path.resolve(__dirname, 'promo-v2.html')}`;
const DURATION  = 31;        // seconds to record (animation ~30.5s)
const TARGET_MS = 33;        // ~30fps target

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

  await page.waitForFunction(() => window.__READY === true, { timeout: 10000 });
  await new Promise(r => setTimeout(r, 700));   // extra settle for fonts

  console.log(`Recording ${DURATION}s @ ~${Math.round(1000/TARGET_MS)}fps...`);

  let frame = 0;
  const start = Date.now();
  const end   = start + DURATION * 1000;

  while (Date.now() < end) {
    const t0  = Date.now();
    const num = String(frame).padStart(5, '0');
    await page.evaluate(() => document.body.getBoundingClientRect());
    await page.screenshot({
      path: `${FRAME_DIR}/f${num}.jpg`,
      type: 'jpeg',
      quality: 95,
      captureBeyondViewport: false,
    });
    frame++;
    const wait = TARGET_MS - (Date.now() - t0);
    if (wait > 1) await new Promise(r => setTimeout(r, wait));
  }

  await browser.close();

  const actualFPS = (frame / DURATION).toFixed(1);
  console.log(`Captured ${frame} frames  →  ${actualFPS} fps`);

  const inFPS = Math.max(1, Math.round(frame / DURATION));
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
