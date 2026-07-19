import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

const targetStr = `            </div>
          ))}
        </div>
      </div>
    </SectionWrapper>
  );
};

const SequentialTypewriter`;

const replacement = `            </div>
          ))}
        </div>
        </div>
      </div>
    </SectionWrapper>
  );
};

const SequentialTypewriter`;

code = code.replace(targetStr, replacement);
fs.writeFileSync('src/App.tsx', code);
