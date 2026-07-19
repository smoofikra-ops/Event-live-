import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

const oldEnd = `          ))}
        </div>
      </div>
    </SectionWrapper>`;

const newEnd = `          ))}
        </div>
        </div>
      </div>
    </SectionWrapper>`;

code = code.replace(oldEnd, newEnd);
fs.writeFileSync('src/App.tsx', code);
