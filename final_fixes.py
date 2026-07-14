import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Fix href template string
content = content.replace(
    'href="https://wa.me/966536753679?text={t(\'contact.whatsappText\')}"',
    'href={`https://wa.me/966536753679?text=${t(\'contact.whatsappText\')}`}'
)

# Fix App component
content = content.replace("export default function App() {\n  const [data, setData] = useState<AppData>(INITIAL_DATA);", "export default function App() {\n  const { t } = useLanguage();\n  const [data, setData] = useState<AppData>(INITIAL_DATA);")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
