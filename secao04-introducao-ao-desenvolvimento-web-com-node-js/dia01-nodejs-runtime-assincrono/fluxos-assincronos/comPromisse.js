function calqDiv (n1, n2) {
    if (n2 === 0) {
      throw new Error('ERRO! não é possivel dividir por zero');
    }
  const div = n1/n2;
  return div;
}

try {
  console.log(calqDiv(1,0))
} catch (e) {
  console.log(e.message)
}

console.log('o codigo chegou ate aqui');