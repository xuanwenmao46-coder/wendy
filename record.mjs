/**
 * Records the infographic animation as a series of PNG frames,
 * then hands off to ffmpeg to produce an MP4.
 */
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { execSync }  from 'child_process';
import { mkdirSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dir   = dirname(fileURLToPath(import.meta.url));
const htmlFile = resolve(__dir, 'infographic-bar-chart.html');
const framesDir = resolve(__dir, 'frames');
const outputMp4 = resolve(__dir, 'infographic-preview.mp4');

const FPS        = 30;
const DURATION_S = 6;       // total capture duration
const TOTAL_FRAMES = FPS * DURATION_S;
const WIDTH  = 1280;
const HEIGHT = 800;

mkdirSync(framesDir, { recursive: true });

console.log('Launching browser…');
const browser = await chromium.launch({
  executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
});

const ctx  = await browser.newContext({ viewport: { width: WIDTH, height: HEIGHT } });
const page = await ctx.newPage();

await page.goto(`file://${htmlFile}`);

// Let the page settle (container fade-in starts at 150ms)
await page.waitForTimeout(300);

console.log(`Capturing ${TOTAL_FRAMES} frames at ${FPS} fps…`);

for (let f = 0; f < TOTAL_FRAMES; f++) {
  const pad = String(f).padStart(5, '0');
  await page.screenshot({ path: `${framesDir}/frame_${pad}.png` });
  // advance time by 1/FPS
  await page.waitForTimeout(1000 / FPS);
  if (f % 30 === 0) process.stdout.write(`  frame ${f}/${TOTAL_FRAMES}\r`);
}

await browser.close();
console.log('\nEncoding MP4 with ffmpeg…');

execSync(
  `ffmpeg -y -framerate ${FPS} -i "${framesDir}/frame_%05d.png" ` +
  `-c:v libx264 -pix_fmt yuv420p -crf 18 -preset slow "${outputMp4}"`,
  { stdio: 'inherit' }
);

console.log(`\nDone → ${outputMp4}`);
