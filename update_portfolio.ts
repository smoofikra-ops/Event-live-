import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

appTsx = appTsx.replace(
  `const getYoutubeEmbedUrl = (url: string) => {
    if (!url) return '';
    const regExp = /^.*(youtu.be\\/|v\\/|u\\/\\w\\/|embed\\/|watch\\?v=|\\&v=)([^#\\&\\?]*).*/;
    const match = url.match(regExp);
    if (match && match[2].length === 11) {
      return \`https://www.youtube.com/embed/\${match[2]}?autoplay=1&mute=1&loop=1&playlist=\${match[2]}\`;
    }
    return '';
  };`,
  `const getYoutubeEmbedUrl = (url: string, isLightbox = false) => {
    if (!url) return '';
    const regExp = /^.*(youtu.be\\/|v\\/|u\\/\\w\\/|embed\\/|watch\\?v=|\\&v=)([^#\\&\\?]*).*/;
    const match = url.match(regExp);
    if (match && match[2].length === 11) {
      return isLightbox 
        ? \`https://www.youtube.com/embed/\${match[2]}?autoplay=1&rel=0\`
        : \`https://www.youtube.com/embed/\${match[2]}?autoplay=1&mute=1&loop=1&playlist=\${match[2]}&controls=0\`;
    }
    return url;
  };`
);

appTsx = appTsx.replace(
  'src={getYoutubeEmbedUrl(selectedWork.videoUrl)}',
  'src={getYoutubeEmbedUrl(selectedWork.videoUrl, true)}'
);

fs.writeFileSync('src/App.tsx', appTsx);
console.log('Portfolio embed url updated!');
