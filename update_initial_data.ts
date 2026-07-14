import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

const updatedInitialData = `const INITIAL_DATA: AppData = {
  heroVideoUrl: '',
  services: [
    { id: '1', title: "المعارض", desc: "نبرز حضوركم المميز من خلال تغطية احترافية تشمل أجنحة الزوار والفعاليات المصاحبة، بواسطة كاميرات احترافية ودرون.", iconName: 'Layout', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&q=80&w=800' },
    { id: '2', title: "المهرجانات", desc: "نوثق أجواء المهرجانات بكل تفاصيلها، من لحظات التفاعل الجماهيري إلى العروض الترفيهية، مع إنتاج فيديوهات مميزة.", iconName: 'Users', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&q=80&w=800' },
    { id: '3', title: "الفعاليات الوطنية", desc: "نعيش معكم روح المناسبة وننقل مشاعر الفخر والانتماء بعدسة فنية، نوثق الفقرات الرسمية والجماهير بأسلوب يليق بالوطن.", iconName: 'Star', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1533174000255-124b17551000?auto=format&fit=crop&q=80&w=800' },
    { id: '4', title: "حفلات الافتتاح", desc: "نحوّل لحظات الافتتاح إلى قصة مرئية تُحكى، نوثق استقبال الضيوف، لحظة قص الشريط، ونصنع فيديو مختصر «هايلايت».", iconName: 'Camera', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&q=80&w=800' },
    { id: '5', title: "المؤتمرات", desc: "نقدم تغطية مؤتمرات ومعارض احترافية، نوثق كل لحظة من الكلمات الرسمية إلى جلسات النقاش، مع إمكانيات البث المباشر.", iconName: 'Radio', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1505373877841-8d25f7d46678?auto=format&fit=crop&q=80&w=800' },
    { id: '6', title: "الفعاليات المؤسسية", desc: "نُقدّم تغطيات احترافية لفعاليات الشركات، المؤتمرات والاجتماعات، مع إبراز الهوية المؤسسية وتوفير خدمة البث المباشر.", iconName: 'Building2', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1515162816999-a0c47dc192f7?auto=format&fit=crop&q=80&w=800' },
    { id: '7', title: "العقارات", desc: "نُبرز جماليات العقار بدقة عالية من الداخل والخارج باستخدام التصوير الأرضي والجوي، مع مونتاج احترافي جاذب.", iconName: 'Home', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=800' },
    { id: '8', title: "الإعلانات التجارية", desc: "نصمم محتوى بصري إبداعي يُبرز كل منتج بأفضل صورة، مع إعداد ستايل تصوير مميز وإخراج احترافي.", iconName: 'Megaphone', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&q=80&w=800' },
  ]`;

appTsx = appTsx.replace(/const INITIAL_DATA: AppData = {[\s\S]*? works:/, updatedInitialData + ',\n  works:');

fs.writeFileSync('src/App.tsx', appTsx);
console.log('INITIAL_DATA updated!');
