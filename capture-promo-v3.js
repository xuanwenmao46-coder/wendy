const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');
const { execSync } = require('child_process');

const FRAMES_DIR = '/tmp/promo-v3-frames';
const OUT_FILE = path.join(__dirname, 'promo-v3.mp4');
const HTML_FILE = 'file://' + path.join(__dirname, 'promo-v3.html');
const DURATION = 30500; // ms — 30.5s to catch final frame
const FRAME_INTERVAL = 67; // ~15fps

if (fs.existsSync(FRAMES_DIR)) execSync(`rm -rf ${FRAMES_DIR}`);
fs.mkdirSync(FRAMES_DIR, { recursive: true });

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-background-timer-throttling',
      '--disable-renderer-backgrounding',
      '--disable-backgrounding-occluded-windows',
      '--force-device-scale-factor=1',
    ],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720, deviceScaleFactor: 1 });

  console.log('Loading page...');
  await page.goto(HTML_FILE, { waitUntil: 'networkidle0' });

  // Wait for GSAP to be ready
  await page.waitForFunction('typeof gsap !== "undefined"', { timeout: 5000 });
  console.log('GSAP ready. Capturing...');

  let frame = 0;
  const start = Date.now();

  while (Date.now() - start < DURATION) {
    const filename = path.join(FRAMES_DIR, `f${String(frame).padStart(5, '0')}.jpg`);
    await page.screenshot({ path: filename, type: 'jpeg', quality: 92 });
    frame++;
    const elapsed = Date.now() - start;
    const nextTarget = frame * FRAME_INTERVAL;
    const wait = nextTarget - elapsed;
    if (wait > 0) await new Promise(r => setTimeout(r, wait));
  }

  await browser.close();
  console.log(`Captured ${frame} frames at ~${(frame / (DURATION / 1000)).toFixed(1)}fps`);

  // Encode with ffmpeg — duplicate frames to reach 30fps output
  const capturedFps = (frame / (DURATION / 1000)).toFixed(2);
  console.log('Encoding...');
  execSync(
    `ffmpeg -y -framerate ${capturedFps} -i ${FRAMES_DIR}/f%05d.jpg ` +
    `-vf "fps=30,scale=1280:720" ` +
    `-c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p ` +
    `${OUT_FILE}`,
    { stdio: 'inherit' }
  );

  execSync(`rm -rf ${FRAMES_DIR}`);
  const size = (fs.statSync(OUT_FILE).size / 1024 / 1024).toFixed(1);
  console.log(`Done: ${OUT_FILE} (${size}MB)`);
})();
