const myRemove = require('../exercícios/exercicios.7.3.2');
it('Verifica a chamada da função myRemove([1, 2, 3, 4], 3) é [1, 2, 4]', () => {
    expect(myRemove([1, 2, 3, 4], 3)).toEqual([1, 2, 4]);

})
it('Verifica a chamada da função myRemove([1, 2, 3, 4], 3) NÃO é [1, 2, 3, 4]', () => {
    expect(myRemove([1, 2, 3, 4], 3)).not.toEqual([1, 2, 3, 4]);

})
it('Verifica a chamada da função myRemove([1, 2, 3, 4], 5) é [1, 2, 3, 4]', () => {
    expect(myRemove([1, 2, 3, 4], 5)).toEqual([1, 2, 3, 4]);

})

