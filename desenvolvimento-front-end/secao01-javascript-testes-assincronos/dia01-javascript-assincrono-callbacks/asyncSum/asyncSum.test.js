const asyncSum = (a, b, callback) => {
    setTimeout(() => {
        const result = a + b;
        callback(result);
    }, 4994);
};
test('Testando asyncSum, soma 5 mais 10', (done) => {
    const func = (result) => {
        try {
            expect(result).toBe(15);
            done();
        } catch (error) {
            done(error);
        }
    };
    asyncSum(5, 10, func);
});
