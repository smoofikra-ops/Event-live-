import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

const targetStr = `  const isYoutube = videoUrl?.includes('youtube.com') || videoUrl?.includes('youtu.be') || videoUrl?.includes('drive.google.com');
  
  const getYoutubeEmbedUrl = (url: string) => {
    if (!url) return '';
    if (url.includes('drive.google.com')) {
      const match = url.match(/\\/d\\/([a-zA-Z0-9_-]+)/);
      if (match) {
        return \`https://drive.google.com/file/d/\${match[1]}/preview?autoplay=1\`;
      }
      return url;
    }`;

const replacement = `  const isYoutube = videoUrl?.includes('youtube.com') || videoUrl?.includes('youtu.be');
  
  const getDirectVideoUrl = (url: string) => {
    if (!url) return '';
    if (url.includes('drive.google.com')) {
      const match = url.match(/\\/d\\/([a-zA-Z0-9_-]+)/);
      if (match) {
        return \`https://drive.google.com/uc?export=download&id=\${match[1]}\`;
      }
    }
    return url;
  };

  const getYoutubeEmbedUrl = (url: string) => {
    if (!url) return '';`;

code = code.replace(targetStr, replacement);

const targetSource = `                {videoUrl && (
                  <>
                    <source src={videoUrl} type="video/quicktime" />
                    <source src={videoUrl} type="video/mp4" />
                    متصفحك لا يدعم تشغيل الفيديو.
                  </>
                )}`;

const replacementSource = `                {videoUrl && (
                  <>
                    <source src={getDirectVideoUrl(videoUrl)} type="video/mp4" />
                    متصفحك لا يدعم تشغيل الفيديو.
                  </>
                )}`;

code = code.replace(targetSource, replacementSource);
fs.writeFileSync('src/App.tsx', code);
