const { expect } = require('chai');
const calculaSituacao = require('../calculaSituacao');
describe('Quando a média for menor que 7', function () {
  it('verifica se a função retorna reprovação caso a nota seja inferior a 7', function () {
    console.log('test')
    const resposta = calculaSituacao(4);
    expect(resposta).equals('reprovação');
  })
});
