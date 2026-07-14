const https = require('https');
https.get('https://api.cloudinary.com/v1_1/ozd726ro/search?expression=collection:a998b2ca26105e0c043b9c2672fb4a86', (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => console.log(data));
});
