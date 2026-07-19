import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

const targetStr = `const Footer = ({ socialLinks }: { socialLinks: SocialLink[] }) => {
  const { t, language } = useLanguage();
  const [openSection, setOpenSection] = useState<string | null>(null);`;

const replacement = `const Footer = ({ socialLinks }: { socialLinks: SocialLink[] }) => {
  const { t, language } = useLanguage();
  const [openSection, setOpenSection] = useState<string | null>(null);
  const [isTermsOpen, setIsTermsOpen] = useState(false);
  const [isPrivacyOpen, setIsPrivacyOpen] = useState(false);`;

code = code.replace(targetStr, replacement);

const targetBottom = `            <p>© {new Date().getFullYear()} EventLive KSA. {t("footer.rights")}</p>
            <div className="flex gap-4">
              <a href="#" className="hover:text-amber-500 transition-colors">{t("footer.terms")}</a>
              <a href="#" className="hover:text-amber-500 transition-colors">{t("footer.privacy")}</a>
            </div>`;

const replacementBottom = `            <p>© {new Date().getFullYear()} EventLive KSA. {t("footer.rights")}</p>
            <div className="flex gap-4 items-center">
              <a href="https://eventliveksa.com" target="_blank" rel="noopener noreferrer" className="hover:text-amber-500 transition-colors">eventliveksa.com</a>
              <span className="text-black/20 dark:text-white/20">|</span>
              <button onClick={(e) => { e.preventDefault(); setIsTermsOpen(true); }} className="hover:text-amber-500 transition-colors">{t("footer.terms")}</button>
              <span className="text-black/20 dark:text-white/20">|</span>
              <button onClick={(e) => { e.preventDefault(); setIsPrivacyOpen(true); }} className="hover:text-amber-500 transition-colors">{t("footer.privacy")}</button>
            </div>
            
            <AnimatePresence>
              {isTermsOpen && (
                <div className="fixed inset-0 z-[200] flex items-center justify-center p-4 sm:p-6" dir={language === 'ar' ? 'rtl' : 'ltr'}>
                  <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="absolute inset-0 bg-black/60 backdrop-blur-sm" onClick={() => setIsTermsOpen(false)} />
                  <motion.div initial={{ opacity: 0, scale: 0.95, y: 20 }} animate={{ opacity: 1, scale: 1, y: 0 }} exit={{ opacity: 0, scale: 0.95, y: 20 }} className="relative w-full max-w-3xl max-h-[85vh] overflow-y-auto bg-white dark:bg-[#111] rounded-2xl shadow-2xl p-6 sm:p-10 border border-black/10 dark:border-white/10 text-right md:text-right ltr:text-left">
                    <button onClick={() => setIsTermsOpen(false)} className="absolute top-4 rtl:left-4 ltr:right-4 rtl:right-auto text-black/50 dark:text-white/50 hover:text-amber-500 transition-colors bg-black/5 dark:bg-white/5 p-2 rounded-full">
                      <X className="w-5 h-5" />
                    </button>
                    <h2 className="text-2xl font-bold mb-6 text-black dark:text-white">{t("footer.terms")}</h2>
                    <div className="space-y-4 text-black/70 dark:text-white/70 text-sm md:text-base leading-relaxed">
                      <p><strong>1. قبول الشروط:</strong> باستخدامك لخدمات EventLive KSA، فإنك توافق على الالتزام بهذه الشروط والأحكام.</p>
                      <p><strong>2. الخدمات:</strong> نقدم خدمات التصوير الفوتوغرافي والفيديو والبث المباشر للفعاليات والمؤتمرات وفقاً لما يتم الاتفاق عليه في عقد الخدمة.</p>
                      <p><strong>3. الدفع والتسعير:</strong> يتم تحديد الأسعار بناءً على متطلبات كل فعالية. يتم دفع عربون لتأكيد الحجز والمبلغ المتبقي قبل تسليم المواد النهائية.</p>
                      <p><strong>4. الملكية الفكرية:</strong> تحتفظ EventLive KSA بحقوق الطبع والنشر للمواد المنتجة ما لم يتم الاتفاق على غير ذلك كتابياً. يحق للعميل استخدام المواد للأغراض المتفق عليها.</p>
                      <p><strong>5. الإلغاء والتعديل:</strong> في حال إلغاء الحجز من قبل العميل قبل موعد الفعالية بفترة قصيرة، قد يتم خصم العربون وفقاً لسياسة الإلغاء الخاصة بنا.</p>
                      <p><strong>6. إخلاء المسؤولية:</strong> نبذل قصارى جهدنا لتقديم أفضل جودة، ولكننا لا نتحمل المسؤولية عن أي ظروف قاهرة خارجة عن إرادتنا (مثل انقطاع التيار الكهربائي في موقع الفعالية).</p>
                    </div>
                  </motion.div>
                </div>
              )}
              {isPrivacyOpen && (
                <div className="fixed inset-0 z-[200] flex items-center justify-center p-4 sm:p-6" dir={language === 'ar' ? 'rtl' : 'ltr'}>
                  <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="absolute inset-0 bg-black/60 backdrop-blur-sm" onClick={() => setIsPrivacyOpen(false)} />
                  <motion.div initial={{ opacity: 0, scale: 0.95, y: 20 }} animate={{ opacity: 1, scale: 1, y: 0 }} exit={{ opacity: 0, scale: 0.95, y: 20 }} className="relative w-full max-w-3xl max-h-[85vh] overflow-y-auto bg-white dark:bg-[#111] rounded-2xl shadow-2xl p-6 sm:p-10 border border-black/10 dark:border-white/10 text-right md:text-right ltr:text-left">
                    <button onClick={() => setIsPrivacyOpen(false)} className="absolute top-4 rtl:left-4 ltr:right-4 rtl:right-auto text-black/50 dark:text-white/50 hover:text-amber-500 transition-colors bg-black/5 dark:bg-white/5 p-2 rounded-full">
                      <X className="w-5 h-5" />
                    </button>
                    <h2 className="text-2xl font-bold mb-6 text-black dark:text-white">{t("footer.privacy")}</h2>
                    <div className="space-y-4 text-black/70 dark:text-white/70 text-sm md:text-base leading-relaxed">
                      <p><strong>1. جمع المعلومات:</strong> نقوم بجمع المعلومات الشخصية التي تقدمها لنا طواعية عند التواصل معنا أو طلب خدماتنا، مثل الاسم، رقم الهاتف، وعنوان البريد الإلكتروني.</p>
                      <p><strong>2. استخدام المعلومات:</strong> نستخدم معلوماتك لتوفير الخدمات المطلوبة، التواصل معك بخصوص حجوزاتك، وتحسين مستوى خدمتنا.</p>
                      <p><strong>3. حماية المعلومات:</strong> نحن نتخذ إجراءات أمنية مناسبة لحماية معلوماتك الشخصية من الوصول غير المصرح به أو التعديل أو الكشف عنها.</p>
                      <p><strong>4. مشاركة المعلومات:</strong> لا نقوم ببيع أو تأجير معلوماتك الشخصية لأطراف ثالثة. قد نشارك معلوماتك فقط مع مزودي الخدمات الذين يساعدوننا في تشغيل أعمالنا (مثل خدمات التخزين السحابي) تحت شروط سرية صارمة.</p>
                      <p><strong>5. استخدام الصور والفيديو:</strong> قد نستخدم مقتطفات من الأعمال التي قمنا بتصويرها في معرض أعمالنا أو على حساباتنا في وسائل التواصل الاجتماعي لأغراض ترويجية، ما لم يطلب العميل كتابياً عدم القيام بذلك.</p>
                      <p><strong>6. التعديلات:</strong> نحتفظ بالحق في تحديث سياسة الخصوصية هذه من وقت لآخر.</p>
                    </div>
                  </motion.div>
                </div>
              )}
            </AnimatePresence>`;

code = code.replace(targetBottom, replacementBottom);
fs.writeFileSync('src/App.tsx', code);
