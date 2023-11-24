const sum = require('../exercícios/exercicios.7.3.1');

test("Verifica a chamada da função sum(4, 5) é 9", ()=> {
    expect(sum(4, 5)).toEqual(9);
})
it("Verifica a chamada da função sum(0, 0) é 0", ()=> {
    expect(sum(0, 0)).toEqual(0);
})
it("verifica o funcionamento do throwNewError", () => {
    expect(() => { sum(4, '5') }).toThrowError();
    expect(() => { sum(4, '5') }).toThrowError('parameters must be numbers');
})
