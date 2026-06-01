const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');
const { execSync } = require('child_process');

const FRAMES_DIR = '/tmp/silence-matter-frames';
const OUT_FILE   = path.join(__dirname, 'silence-of-matter.mp4');
const HTML_FILE  = 'file://' + path.join(__dirname, 'silence-of-matter.html');
const DURATION   = 45500;   // 45.5s
const INTERVAL   = 67;      // ~15fps

if (fs.existsSync(FRAMES_DIR)) execSync(`rm -rf ${FRAMES_DIR}`);
fs.mkdirSync(FRAMES_DIR, { recursive: true });

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: [
      '--no-sandbox', '--disable-setuid-sandbox',
      '--disable-background-timer-throttling',
      '--disable-renderer-backgrounding',
      '--disable-backgrounding-occluded-windows',
      '--force-device-scale-factor=1',
    ],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720, deviceScaleFactor: 1 });

  console.log('Loading silence-of-matter.html...');
  await page.goto(HTML_FILE, { waitUntil: 'networkidle0' });
  await page.waitForFunction('typeof gsap !== "undefined"', { timeout: 5000 });
  console.log('Capturing 45.5s...');

  let frame = 0;
  const start = Date.now();

  while (Date.now() - start < DURATION) {
    const filename = path.join(FRAMES_DIR, `f${String(frame).padStart(5,'0')}.jpg`);
    await page.screenshot({ path: filename, type: 'jpeg', quality: 96 });
    frame++;
    const wait = frame * INTERVAL - (Date.now() - start);
    if (wait > 0) await new Promise(r => setTimeout(r, wait));
  }

  await browser.close();
  const fps = (frame / (DURATION / 1000)).toFixed(2);
  console.log(`Captured ${frame} frames @ ${fps}fps`);

  console.log('Encoding...');
  execSync(
    `ffmpeg -y -framerate ${fps} -i ${FRAMES_DIR}/f%05d.jpg ` +
    `-vf "fps=24,scale=1280:720" ` +
    `-c:v libx264 -preset slow -crf 14 -pix_fmt yuv420p ` +
    `${OUT_FILE}`,
    { stdio: 'inherit' }
  );

  execSync(`rm -rf ${FRAMES_DIR}`);
  const size = (fs.statSync(OUT_FILE).size / 1024 / 1024).toFixed(1);
  console.log(`Done: ${OUT_FILE} (${size}MB)`);
})();
