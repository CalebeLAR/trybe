function divisão (num1, num2) {
  const promisse = new Promise((resolve, reject) => {
    if(num2 == 0) reject(Error("Não pode dividir por zero"));

    const divisão = num1/num2;

    resolve(divisão);
  });

  return promisse;
}

divisão(2,0)
  .then((resolve) => console.log(resolve))
  .catch((reject) => console.log(reject.message));

console.log('chegou ate aqui')