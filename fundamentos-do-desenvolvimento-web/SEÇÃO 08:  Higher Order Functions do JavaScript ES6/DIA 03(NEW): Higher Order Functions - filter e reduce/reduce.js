const valorItens = [1, 32, 44, 2, 3];

valorItens.reduce((acc, curr) => {
  return acc + curr;
});

const numbers = [50, 93, -30, 93, 15];

numbers.find((number, i)=> {
  const isBiger = numbers.every(element => number >= element);
  if (isBiger) {
    return number;
  }
});

const biger = numbers.reduce((bigger, number) => {
  return bigger > number ? bigger : number
});

const numbersParOuImpar = [18, 19, 23, 53, 4, 5, 76, 23, 54];
const somaPares = numbersParOuImpar.reduce((sumPar, number, i)=> {
  return (number % 2) ? sumPar : sumPar + number;
}, 0);

