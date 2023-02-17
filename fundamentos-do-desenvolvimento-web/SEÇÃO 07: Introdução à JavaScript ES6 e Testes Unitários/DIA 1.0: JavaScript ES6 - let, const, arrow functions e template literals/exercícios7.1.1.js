// 🚀 Altere as variáveis para respeitarem o escopo em que foram declaradas.
// Modifique a estrutura da função para que ela seja uma arrow function;
// Modifique as variáveis para que respeitem o escopo onde estão declaradas;
// Modifique as concatenações para template literals.

const testingScope = escopo => {
    if (escopo === true) {
      let ifScope = 'Não devo ser utilizada fora do meu escopo (if)';
      console.log(`${ifScope} ótimo, fui utilizada no escopo !`);
    } else {
      let elseScope = 'Não devo ser utilizada fora meu escopo (else)';
      console.log(elseScope);
    }
  }

  testingScope(true);

// const testingScope = escopo => {
//     (escopo === true)? console.log(`Não devo ser utilizada fora do meu escopo (if) ótimo, fui utilizada no escopo !`): console.log("Não devo ser utilizada fora meu escopo (else)");
// }
// testingScope(true)


// 🚀 Crie uma função que retorne um array em ordem crescente.

// Seu código aqui.
const ordena = array => array.sort((a, b) => a - b)
const oddsAndEvens = [13, 3, 4, 10, 7, 2];
console.log(`Os números ${ordena(oddsAndEvens)} se encontram ordenados de forma crescente!`);

// Crie uma função que faça com que o array oddsAndEvens fique na ordem crescente;
// Utilize o console.log e template literals para retornar a frase: 'Os números 2,3,4,7,10,13 se encontram ordenados de forma crescente!'.
// Bônus (opcional): tente fazer o mesmo exercício utilizando o método array.sort(). Spoiler: É possível realizar uma função que ordene qualquer array de números.
