import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Add AnnouncementBanner
old_app_start = """      <ScrollProgress />
      <MouseFollower />
      <Sidebar onAdminClick={() => setIsAdminOpen(!isAdminOpen)} isAdminMode={isAdminOpen} onQuoteClick={() => setIsQuoteOpen(true)} />"""

new_app_start = """      <AnnouncementBanner />
      <ScrollProgress />
      <MouseFollower />
      <Sidebar onAdminClick={() => setIsAdminOpen(!isAdminOpen)} isAdminMode={isAdminOpen} onQuoteClick={() => setIsQuoteOpen(true)} />"""

content = content.replace(old_app_start, new_app_start)

# Change Desktop Nav top
content = content.replace(
    """<div className="hidden md:flex fixed top-0 left-0 right-0 z-[90] h-20 items-center px-8 bg-white/60 dark:bg-[#0a0a0a]/60 backdrop-blur-xl border-b border-black/10 dark:border-white/10 shadow-sm transition-all justify-between">""",
    """<div className="hidden md:flex fixed top-10 left-0 right-0 z-[90] h-20 items-center px-8 bg-white/60 dark:bg-[#0a0a0a]/60 backdrop-blur-xl border-b border-black/10 dark:border-white/10 shadow-sm transition-all justify-between">"""
)

# Change Mobile Nav top
content = content.replace(
    """<div className="md:hidden fixed top-0 left-0 right-0 z-[100] h-16 flex items-center justify-between px-4 bg-white/60 dark:bg-[#0a0a0a]/60 backdrop-blur-xl border-b border-black/10 dark:border-white/10 shadow-sm">""",
    """<div className="md:hidden fixed top-10 left-0 right-0 z-[100] h-16 flex items-center justify-between px-4 bg-white/60 dark:bg-[#0a0a0a]/60 backdrop-blur-xl border-b border-black/10 dark:border-white/10 shadow-sm">"""
)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
