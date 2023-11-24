const names = ['Mateus', 'José', 'Ana', 'Cláudia', 'Bruna'];

const hasName = (arr, name) => arr.some((nomeNoArray) => (nomeNoArray === name));

console.log(hasName(names, 'José'));