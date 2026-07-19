import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

const oldProcessEnd = `              <p className="text-[10px] sm:text-xs md:text-base text-black/60 dark:text-white/60 hidden sm:block">{step.desc}</p>
            </ScrollReveal>
          ))}
        </div>
        </div>
      </div>
    </SectionWrapper>
  );
};`;

const newProcessEnd = `              <p className="text-[10px] sm:text-xs md:text-base text-black/60 dark:text-white/60 hidden sm:block">{step.desc}</p>
            </ScrollReveal>
          ))}
        </div>
      </div>
    </SectionWrapper>
  );
};`;

code = code.replace(oldProcessEnd, newProcessEnd);
fs.writeFileSync('src/App.tsx', code);
