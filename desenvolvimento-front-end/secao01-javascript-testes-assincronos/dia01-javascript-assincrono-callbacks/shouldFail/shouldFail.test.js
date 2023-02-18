// shouldFail.test.js
const tenta = () => { 
    try {
        expect(5).toBe(5);
        console.log('Deveria falhar!');
        done();
      } catch (error) {
        done();
      }
};

test('Não deveria passar!', (done) => {
    setTimeout(() => {
        // tenta(); // expect e done só funcionam dentro do escopo de test.
        try {
            expect(50).toBe(5);
            console.log('Deveria falhar!');
            done();
          } catch (error) {
            done(error);
          }
    }, 500);
  });