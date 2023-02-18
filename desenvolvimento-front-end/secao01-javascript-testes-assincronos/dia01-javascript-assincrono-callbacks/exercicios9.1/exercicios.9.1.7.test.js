//Código da questão 7.


const uppercase = (str, callback) => {
  setTimeout(() => {
    const paran = str.toUpperCase();
    callback(paran);
  }, 500);
};

test('Verifica se uppercase("string em minúsculas", returnLetters) retorna a string: STRING EM MINÚSCULAS', (done) => {
  const calb = (stringDaHOF) => {
    try {
      expect(stringDaHOF).toBe("STRING EM MINÚSCULAS");
      done();
    } catch (error) {
      done(error)
    }
  };
  uppercase("string em minúsculas", calb)
});
