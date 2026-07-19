import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

const oldPartnersEnd = `              <div className="absolute inset-0 opacity-0 dark:opacity-100 pointer-events-none transition-all duration-500 overflow-hidden rounded-2xl">
                <div className="absolute -top-1/2 -left-1/2 w-full h-full bg-amber-500/10 blur-2xl transform group-hover/card:scale-150 transition-transform duration-700"></div>
                <div className="absolute -bottom-1/2 -right-1/2 w-full h-full bg-blue-500/10 blur-2xl transform group-hover/card:scale-150 transition-transform duration-700"></div>
              </div>
              
              <img 
                src={getOptimizedImageUrl(p.logo)} 
                alt={p.name} 
                className="w-full h-full object-cover relative z-10 transition-transform duration-500 group-hover/card:scale-110"
                loading="lazy" />
            </div>
          ))}
        </div>
      </div>
    </SectionWrapper>
  );
};`;

const newPartnersEnd = `              <div className="absolute inset-0 opacity-0 dark:opacity-100 pointer-events-none transition-all duration-500 overflow-hidden rounded-2xl">
                <div className="absolute -top-1/2 -left-1/2 w-full h-full bg-amber-500/10 blur-2xl transform group-hover/card:scale-150 transition-transform duration-700"></div>
                <div className="absolute -bottom-1/2 -right-1/2 w-full h-full bg-blue-500/10 blur-2xl transform group-hover/card:scale-150 transition-transform duration-700"></div>
              </div>
              
              <img 
                src={getOptimizedImageUrl(p.logo)} 
                alt={p.name} 
                className="w-full h-full object-cover relative z-10 transition-transform duration-500 group-hover/card:scale-110"
                loading="lazy" />
            </div>
          ))}
        </div>
        </div>
      </div>
    </SectionWrapper>
  );
};`;

code = code.replace(oldPartnersEnd, newPartnersEnd);
fs.writeFileSync('src/App.tsx', code);
