const jsonInfo = `{
    "muitasEmpresasUsam": [
      "Google",
      "Twitter",
      "Facebook",
      "etc..."
    ],
    "temVariasVantagens": [
      "Legível",
      "Fácil de usar",
      "Leve",
      "Popular",
      "Versátil"
    ],
    "muitasLinguagensDaoSuporte": [
      "Python",
      "C",
      "C++",
      "Java",
      "PHP"
    ],
    "Object": 
    {
    "nome": "calebe",
    "sobrenome": "ribeiro",
    "estado": "Roraima",
    "escolas": ["vmc", "arco-íris", "GD"]
    }
  }`;
  
  const usoJSONPorque = JSON.parse(jsonInfo);
  console.log(usoJSONPorque.Object)
  
  const corporationsList = document.getElementById('corporations-used-by');
  const advantagesList = document.getElementById('advantages');
  const languagesList = document.getElementById('languages-used-by');
  
  usoJSONPorque.muitasEmpresasUsam.map((empresa) => {
    const newLi = document.createElement('li');
    newLi.innerText = empresa;
    corporationsList.appendChild(newLi);
  });
  
  usoJSONPorque.temVariasVantagens.map((vantagens) => {
    const newLi = document.createElement('li');
    newLi.innerText = vantagens;
    advantagesList.appendChild(newLi);
  });
  
  usoJSONPorque.muitasLinguagensDaoSuporte.map((linguagens) => {
    const newLi = document.createElement('li');
    newLi.innerText = linguagens;
    languagesList.appendChild(newLi);
  });
  const section = document.createElement('section');
  const body = document.querySelector('body');
  body.appendChild(section);
  usoJSONPorque.muitasEmpresasUsam.map((empresa)=>{
    const quadradinho = document.createElement('div');
    quadradinho.style.display = 'inline-block';
    quadradinho.style.width = '120px';
    quadradinho.style.height = '120px';
    quadradinho.style.textAlign = 'center'
    quadradinho.style.border = '5px solid black';
    quadradinho.innerHTML = empresa;
    section.appendChild(quadradinho);
  });