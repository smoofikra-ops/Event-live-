import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Footer component
old_footer_start = """const Footer = ({ socialLinks }: { socialLinks: SocialLink[] }) => {
  const { t, language } = useLanguage();
  return (
    <footer className="relative bg-white/50 dark:bg-[#020202]/80 backdrop-blur-3xl border-t border-black/5 dark:border-white/5 pt-20 pb-10 overflow-hidden">"""

new_footer_start = """const Footer = ({ socialLinks }: { socialLinks: SocialLink[] }) => {
  const { t, language } = useLanguage();
  const [openSection, setOpenSection] = useState<string | null>(null);

  const toggleSection = (section: string) => {
    setOpenSection(openSection === section ? null : section);
  };
  
  return (
    <footer className="relative bg-white/50 dark:bg-[#020202]/80 backdrop-blur-3xl border-t border-black/5 dark:border-white/5 pt-12 md:pt-20 pb-10 overflow-hidden">"""

content = content.replace(old_footer_start, new_footer_start)

old_grid = """      <div className="max-w-7xl mx-auto px-6 relative z-10">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
          <div>
            <a href="#home" className="flex items-center gap-2 mb-6">
              <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-12 object-contain drop-shadow-[0_0_15px_rgba(255,138,0,0.3)]" />
            </a>
            <p className="text-black/60 dark:text-white/60 mb-6 leading-relaxed">
              {t("footer.companyDesc")}
            </p>
          </div>
          <div>
            <h4 className="font-bold text-lg mb-6 text-black dark:text-white">{t("footer.quickLinks")}</h4>
            <HoverLinkGroup id={`footer-group-${Math.random()}`} links={[
              { label: t("nav.home"), href: "#home" },
              { label: t("nav.services"), href: "#services" },
              { label: t("nav.portfolio"), href: "#portfolio" },
              { label: t("nav.faq"), href: "#faq" }
            ]} />
          </div>
          <div>
            <h4 className="font-bold text-lg mb-6 text-black dark:text-white">{t("nav.services")}</h4>
            <HoverLinkGroup id={`footer-group-${Math.random()}`} links={[
              { label: t("footer.service1"), href: "#" },
              { label: t("footer.service2"), href: "#" },
              { label: t("footer.service3"), href: "#" },
              { label: t("footer.service4"), href: "#" }
            ]} />
          </div>
          <div>
            <h4 className="font-bold text-lg mb-6 text-black dark:text-white">{t("contact.title")}</h4>
            
            <div className="flex flex-col gap-4 mb-6">
              <a href="tel:+966500000000" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors relative z-10 pointer-events-auto">
                <div className="w-8 h-8 rounded-full bg-black/5 dark:bg-white/5 flex items-center justify-center text-amber-500">
                  <Phone className="w-4 h-4" />
                </div>
                <span className="font-medium text-sm" dir="ltr">+966 50 000 0000</span>
              </a>
              <a href="mailto:info@eventliveksa.com" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors relative z-10 pointer-events-auto">
                <div className="w-8 h-8 rounded-full bg-black/5 dark:bg-white/5 flex items-center justify-center text-amber-500">
                  <Mail className="w-4 h-4" />
                </div>
                <span className="font-medium text-sm" dir="ltr">info@eventliveksa.com</span>
              </a>
            </div>"""

new_grid = """      <div className="max-w-7xl mx-auto px-6 relative z-10">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-12 mb-16">
          <div className="mb-4 md:mb-0">
            <a href="#home" className="flex items-center gap-2 mb-6">
              <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-12 object-contain drop-shadow-[0_0_15px_rgba(255,138,0,0.3)]" />
            </a>
            <p className="text-black/60 dark:text-white/60 mb-6 leading-relaxed">
              {t("footer.companyDesc")}
            </p>
          </div>
          
          <div className="border-b border-black/10 dark:border-white/10 md:border-none pb-4 md:pb-0">
            <button 
              onClick={() => toggleSection('quickLinks')}
              className="flex justify-between items-center w-full md:cursor-auto"
            >
              <h4 className="font-bold text-lg text-black dark:text-white md:mb-6">{t("footer.quickLinks")}</h4>
              <ChevronDown className={`w-5 h-5 md:hidden transition-transform duration-300 ${openSection === 'quickLinks' ? 'rotate-180' : ''}`} />
            </button>
            <div className={`mt-4 md:mt-0 overflow-hidden transition-all duration-300 ${openSection === 'quickLinks' ? 'max-h-96' : 'max-h-0 md:max-h-full'}`}>
              <HoverLinkGroup id={`footer-group-${Math.random()}`} links={[
                { label: t("nav.home"), href: "#home" },
                { label: t("nav.services"), href: "#services" },
                { label: t("nav.portfolio"), href: "#portfolio" },
                { label: t("nav.faq"), href: "#faq" }
              ]} />
            </div>
          </div>
          
          <div className="border-b border-black/10 dark:border-white/10 md:border-none pb-4 md:pb-0">
            <button 
              onClick={() => toggleSection('services')}
              className="flex justify-between items-center w-full md:cursor-auto"
            >
              <h4 className="font-bold text-lg text-black dark:text-white md:mb-6">{t("nav.services")}</h4>
              <ChevronDown className={`w-5 h-5 md:hidden transition-transform duration-300 ${openSection === 'services' ? 'rotate-180' : ''}`} />
            </button>
            <div className={`mt-4 md:mt-0 overflow-hidden transition-all duration-300 ${openSection === 'services' ? 'max-h-96' : 'max-h-0 md:max-h-full'}`}>
              <HoverLinkGroup id={`footer-group-${Math.random()}`} links={[
                { label: t("footer.service1"), href: "#" },
                { label: t("footer.service2"), href: "#" },
                { label: t("footer.service3"), href: "#" },
                { label: t("footer.service4"), href: "#" }
              ]} />
            </div>
          </div>
          
          <div className="pb-4 md:pb-0">
            <button 
              onClick={() => toggleSection('contact')}
              className="flex justify-between items-center w-full md:cursor-auto"
            >
              <h4 className="font-bold text-lg text-black dark:text-white md:mb-6">{t("contact.title")}</h4>
              <ChevronDown className={`w-5 h-5 md:hidden transition-transform duration-300 ${openSection === 'contact' ? 'rotate-180' : ''}`} />
            </button>
            
            <div className={`mt-4 md:mt-0 overflow-hidden transition-all duration-300 ${openSection === 'contact' ? 'max-h-96' : 'max-h-0 md:max-h-full'}`}>
              <div className="flex flex-col gap-4 mb-6">
                <a href="tel:+966500000000" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors relative z-10 pointer-events-auto">
                  <div className="w-8 h-8 rounded-full bg-black/5 dark:bg-white/5 flex items-center justify-center text-amber-500">
                    <Phone className="w-4 h-4" />
                  </div>
                  <span className="font-medium text-sm" dir="ltr">+966 50 000 0000</span>
                </a>
                <a href="mailto:info@eventliveksa.com" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors relative z-10 pointer-events-auto">
                  <div className="w-8 h-8 rounded-full bg-black/5 dark:bg-white/5 flex items-center justify-center text-amber-500">
                    <Mail className="w-4 h-4" />
                  </div>
                  <span className="font-medium text-sm" dir="ltr">info@eventliveksa.com</span>
                </a>
              </div>"""

content = content.replace(old_grid, new_grid)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
