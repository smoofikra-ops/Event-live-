import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

const targetStr = `                loading="lazy" />
            </div>
          ))}
        </div>
      </div>
    </SectionWrapper>`;

const replacement = `                loading="lazy" />
            </div>
          ))}
        </div>
        </div>
      </div>
    </SectionWrapper>`;

code = code.replace(targetStr, replacement);
fs.writeFileSync('src/App.tsx', code);
