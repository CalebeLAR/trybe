const fetch = require('node-fetch');

const getRandomAsvice = async () => {
  const url = 'https://api.advicslip.com/advice';
  const request = await fetch(url);
  console.log(request);
};

getRandomAsvice()
