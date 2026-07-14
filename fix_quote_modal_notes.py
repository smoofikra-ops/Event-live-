import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_quote_start = """const QuoteModal = ({ isOpen, onClose }: { isOpen: boolean, onClose: () => void }) => {
  const { t, language } = useLanguage();
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    clientType: '',
    eventType: ''
  });
  const [errors, setErrors] = useState<Record<string, string>>({});

  if (!isOpen) return null;

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    if (errors[e.target.name]) {
      setErrors({ ...errors, [e.target.name]: '' });
    }
  };

  const handleSubmit = (e: React.FormEvent) => {"""

new_quote_start = """const QuoteModal = ({ isOpen, onClose }: { isOpen: boolean, onClose: () => void }) => {
  const { t, language } = useLanguage();
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    clientType: '',
    eventType: '',
    notes: ''
  });
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [isListening, setIsListening] = useState(false);
  const recognitionRef = React.useRef<any>(null);

  React.useEffect(() => {
    return () => {
      if (recognitionRef.current) {
        recognitionRef.current.stop();
      }
    };
  }, []);

  if (!isOpen) return null;

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    if (errors[e.target.name]) {
      setErrors({ ...errors, [e.target.name]: '' });
    }
  };

  const toggleListening = () => {
    if (isListening) {
      recognitionRef.current?.stop();
      setIsListening(false);
      return;
    }

    const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
    if (!SpeechRecognition) {
      alert("عذراً، متصفحك لا يدعم تحويل الصوت إلى نص.");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = language === 'ar' ? 'ar-SA' : 'en-US';
    recognition.interimResults = true;
    recognition.continuous = true;

    recognition.onstart = () => {
      setIsListening(true);
    };

    let startNotes = formData.notes;

    recognition.onresult = (event: any) => {
      let interimTranscript = '';
      let finalTranscript = '';

      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          finalTranscript += event.results[i][0].transcript;
        } else {
          interimTranscript += event.results[i][0].transcript;
        }
      }

      const separator = startNotes && startNotes.trim().length > 0 ? ' ' : '';
      const newNotes = startNotes + separator + finalTranscript + interimTranscript;
      
      setFormData(prev => ({
        ...prev,
        notes: newNotes
      }));

      if (finalTranscript) {
        startNotes += separator + finalTranscript;
      }
    };

    recognition.onerror = (event: any) => {
      console.error(event.error);
      setIsListening(false);
    };

    recognition.onend = () => {
      setIsListening(false);
    };

    recognitionRef.current = recognition;
    recognition.start();
  };

  const handleSubmit = (e: React.FormEvent) => {"""

content = content.replace(old_quote_start, new_quote_start)

old_message = 'const message = `*{t("quote.title")} جديد*\\nالاسم: ${formData.name}\\nالبريد: ${formData.email}\\nالهاتف: ${formData.phone}\\nنوع العميل: ${formData.clientType}\\nنوع الفعالية: ${formData.eventType}`;'
new_message = 'const message = `*${t("quote.title")} جديد*\\nالاسم: ${formData.name}\\nالبريد: ${formData.email}\\nالهاتف: ${formData.phone}\\nنوع العميل: ${formData.clientType}\\nنوع الفعالية: ${formData.eventType}\\nملاحظات: ${formData.notes}`;'

content = content.replace(old_message, new_message)

old_form_end = """              {errors.eventType && <p className="text-red-500 text-xs mt-1">{errors.eventType}</p>}
            </div>
          </div>
          <button type="submit" className="w-full py-4 mt-6 bg-amber-500 text-black font-bold text-lg rounded-xl hover:shadow-[0_0_30px_rgba(255,138,0,0.4)] hover:bg-amber-400 transition-all flex items-center justify-center gap-2">
            {t("quote.submit")}
          </button>
        </form>"""

new_form_end = """              {errors.eventType && <p className="text-red-500 text-xs mt-1">{errors.eventType}</p>}
            </div>
          </div>
          
          <div>
            <div className="flex items-center justify-between mb-2">
              <label className="block text-sm font-bold text-black/80 dark:text-white/80">{language === 'ar' ? 'ملاحظات إضافية' : 'Additional Notes'}</label>
              <button 
                type="button"
                onClick={toggleListening}
                className={`p-2 rounded-full flex items-center justify-center transition-colors ${isListening ? 'bg-red-500 text-white animate-pulse' : 'bg-black/5 dark:bg-white/5 text-black/60 dark:text-white/60 hover:text-amber-500 hover:bg-black/10 dark:hover:bg-white/10'}`}
                title={language === 'ar' ? 'تحدث لإضافة ملاحظات' : 'Speak to add notes'}
              >
                <Mic className="w-4 h-4" />
              </button>
            </div>
            <textarea 
              name="notes" 
              value={formData.notes} 
              onChange={handleChange} 
              rows={3}
              placeholder={language === 'ar' ? 'اكتب أو تحدث هنا...' : 'Write or speak here...'}
              className="w-full bg-black/5 dark:bg-white/5 border border-black/10 dark:border-white/10 rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors text-black dark:text-white resize-none"
            ></textarea>
          </div>

          <button type="submit" className="w-full py-4 mt-6 bg-amber-500 text-black font-bold text-lg rounded-xl hover:shadow-[0_0_30px_rgba(255,138,0,0.4)] hover:bg-amber-400 transition-all flex items-center justify-center gap-2">
            {t("quote.submit")}
          </button>
        </form>"""

content = content.replace(old_form_end, new_form_end)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
