import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_code = """            </div>
          </div>
        </div>
        <div className="border-t border-black/5 dark:border-white/5 pt-8 flex flex-col items-center gap-4 text-sm text-black/40 dark:text-white/40">"""

new_code = """            </div>
            </div>
          </div>
        </div>
        <div className="border-t border-black/5 dark:border-white/5 pt-8 flex flex-col items-center gap-4 text-sm text-black/40 dark:text-white/40">"""

content = content.replace(old_code, new_code)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
