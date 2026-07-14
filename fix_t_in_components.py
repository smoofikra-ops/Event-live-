import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("const FAQ = () => {", "const FAQ = () => {\n  const { t } = useLanguage();")
content = content.replace("const Partners = ({ partners = [] }: { partners?: Partner[] }) => {", "const Partners = ({ partners = [] }: { partners?: Partner[] }) => {\n  const { t } = useLanguage();")
content = content.replace("const QuoteModal = ({ isOpen, onClose }: { isOpen: boolean, onClose: () => void }) => {", "const QuoteModal = ({ isOpen, onClose }: { isOpen: boolean, onClose: () => void }) => {\n  const { t } = useLanguage();")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
