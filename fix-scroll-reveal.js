import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

const oldFaqMap = `{faqs.map((faq, i) => (
          <details key={i} className="group glass-card overflow-hidden transition-all duration-500 open:bg-black/5 dark:bg-white/5 border border-black/10 dark:border-white/10 hover:border-amber-500/30 rounded-xl">`;

const newFaqMap = `{faqs.map((faq, i) => (
          <ScrollReveal key={i} delay={i * 0.1}>
          <details className="group glass-card overflow-hidden transition-all duration-500 open:bg-black/5 dark:bg-white/5 border border-black/10 dark:border-white/10 hover:border-amber-500/30 rounded-xl">`;

code = code.replace(oldFaqMap, newFaqMap);

const oldFaqMapEnd = `</details>
        ))}`;

const newFaqMapEnd = `</details>
          </ScrollReveal>
        ))}`;

code = code.replace(oldFaqMapEnd, newFaqMapEnd);

fs.writeFileSync('src/App.tsx', code);
