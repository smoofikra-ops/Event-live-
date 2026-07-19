import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

// For Services component, let's make it check if it's youtube or drive and render accordingly
const servicesTarget = `              <iframe
                src={selectedVideo}
                className="w-full h-full pointer-events-auto"
                allow="autoplay; encrypted-media; fullscreen; picture-in-picture"
                allowFullScreen
              ></iframe>`;

const servicesReplacement = `              {(() => {
                const isYt = selectedVideo.includes('youtube.com') || selectedVideo.includes('youtu.be');
                const isDrive = selectedVideo.includes('drive.google.com');
                let src = selectedVideo;
                if (isDrive) {
                  const match = selectedVideo.match(/\\/d\\/([a-zA-Z0-9_-]+)/);
                  if (match) src = \`https://drive.google.com/uc?export=download&id=\${match[1]}\`;
                }
                
                return isYt ? (
                  <iframe
                    src={selectedVideo}
                    className="w-full h-full pointer-events-auto"
                    allow="autoplay; encrypted-media; fullscreen; picture-in-picture"
                    allowFullScreen
                  ></iframe>
                ) : (
                  <video
                    src={src}
                    autoPlay
                    controls
                    playsInline
                    className="w-full h-full object-contain pointer-events-auto"
                  ></video>
                );
              })()}`;

code = code.replace(servicesTarget, servicesReplacement);

// For Portfolio component
const portfolioTarget1 = `const Portfolio = ({ works: initialWorks }: { works: Work[] }) => {
  const { t, language } = useLanguage();
  const [filter, setFilter] = useState('الكل');
  const [works, setWorks] = useState(initialWorks);
  const [selectedWork, setSelectedWork] = useState<Work | null>(null);
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null);

  const isYoutube = (url: string) => url.includes('youtube.com') || url.includes('youtu.be') || url.includes('drive.google.com');

  const getYoutubeEmbedUrl = (url: string, isLightbox = false) => {
    if (!url) return '';
    if (url.includes('drive.google.com')) {
      const match = url.match(/\\/d\\/([a-zA-Z0-9_-]+)/);
      if (match) {
        return \`https://drive.google.com/file/d/\${match[1]}/preview?autoplay=1\`;
      }
      return url;
    }`;

const portfolioReplacement1 = `const Portfolio = ({ works: initialWorks }: { works: Work[] }) => {
  const { t, language } = useLanguage();
  const [filter, setFilter] = useState('الكل');
  const [works, setWorks] = useState(initialWorks);
  const [selectedWork, setSelectedWork] = useState<Work | null>(null);
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null);

  const isYoutube = (url: string) => url.includes('youtube.com') || url.includes('youtu.be');

  const getDirectVideoUrl = (url: string) => {
    if (!url) return '';
    if (url.includes('drive.google.com')) {
      const match = url.match(/\\/d\\/([a-zA-Z0-9_-]+)/);
      if (match) return \`https://drive.google.com/uc?export=download&id=\${match[1]}\`;
    }
    return url;
  };

  const getYoutubeEmbedUrl = (url: string, isLightbox = false) => {
    if (!url) return '';`;

code = code.replace(portfolioTarget1, portfolioReplacement1);

// Replace src={w.videoUrl} and src={selectedWork.videoUrl} with getDirectVideoUrl
code = code.replace(/<video \n            src={w.videoUrl}/g, '<video \n            src={getDirectVideoUrl(w.videoUrl!)}');
code = code.replace(/<video \n                    src={selectedWork.videoUrl}/g, '<video \n                    src={getDirectVideoUrl(selectedWork.videoUrl!)}');

fs.writeFileSync('src/App.tsx', code);
