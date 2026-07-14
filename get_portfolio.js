import puppeteer from 'puppeteer-core';
import fs from 'fs';

(async () => {
  const browserPath = fs.readdirSync('./chrome').find(f => f.startsWith('linux-'));
  const executablePath = `./chrome/${browserPath}/chrome-linux64/chrome`;
  
  const browser = await puppeteer.launch({
    executablePath,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  page.on('response', async response => {
    const url = response.url();
    if (url.includes('api.cloudinary.com')) {
      try {
        const json = await response.json();
        fs.writeFileSync('cloudinary_api_portfolio.json', JSON.stringify(json, null, 2));
      } catch (e) {}
    }
  });

  await page.goto('https://collection.cloudinary.com/ozd726ro/19005e2ae38998890938f92fe0a24017', { waitUntil: 'networkidle0' });
  
  const imgs = await page.evaluate(() => Array.from(document.querySelectorAll('img')).map(img => img.src));
  fs.writeFileSync('cloudinary_imgs_portfolio.json', JSON.stringify(imgs, null, 2));
  
  await browser.close();
})();
