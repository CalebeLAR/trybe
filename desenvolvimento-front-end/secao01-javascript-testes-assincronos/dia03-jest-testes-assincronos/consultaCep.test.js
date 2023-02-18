const { consultaCep } = require('./consultaCep.js');

test('tentando com o function', async function () {
    // const resposta = await consultaCep('3013001');
    expect(await consultaCep('30130010')).toBe('Praça Sete de Setembro');
});