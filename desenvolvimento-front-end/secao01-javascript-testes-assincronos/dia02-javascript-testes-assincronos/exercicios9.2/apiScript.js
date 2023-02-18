const API_URL = 'https://icanhazdadjoke.com/';

const fetchJoke = () => {
  const myObject = {
    method: 'GET',
    headers: {'Accept': 'application/json'}
  };

  fetch(API_URL, myObject)
    .then((request)=>(request.json()))
    .then((data)=>{
      const joke = data.joke;
      injecJoke(joke)
    });
  };
  
  const injecJoke = (joke) => {
    const j = document.getElementById('jokeContainer');
    const p = document.createElement('p');
    p.innerText = joke;
    p.style.fontSize = '15px'
    p.style.fontFamily = 'arial'
    j.appendChild(p)
};

window.onload = () => fetchJoke();
