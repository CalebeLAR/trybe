const fetch = require('node-fetch');

const fetchJoke = () => {
  const url = 'https://api.advicslip.com/advice';
  
  const request = fetch(url)
    .then((response) => response.json())
    .then(({slip: {id, advice}})=>(console.log(advice)))
    .catch((error)=> console.log(error));
};

fetchJoke();