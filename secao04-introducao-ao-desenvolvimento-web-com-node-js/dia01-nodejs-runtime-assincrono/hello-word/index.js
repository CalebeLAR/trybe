const readline = require('readline-sync');

const name = readline.question('Qual seu nome? ');
const age = readline.questionInt('Qual sua idade? ');
const animal = readline.question('Qual é o seu animal de estimação? ')
console.log(`Olé, ${name}! Você tem ${age} anos de idade e seu animal de estimação é um ${animal}`);

