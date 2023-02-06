// Verifique se a importação do arquivo correto está sendo feita.
const { getPokemonDetails } = require('./exercicios.9.1.8.js');

describe('A função getPokemonDetails', () => {

  it('retorna erro quando procuramos um pokémon que não existe no banco de dados', (done) => {
    const throwErr = new Error('Não temos esse pokémon para você :(');

    const callback = (error, message) => {
      try {
        expect(error).toEqual(throwErr);
        done();
      } catch (error) {
        done(error);
      }
    };

    getPokemonDetails('pokemonNãoListado', callback);
  });

  it('retorna um pokémon que existe no banco de dados', (done) => {
    const pokemonsListados = [
      {
        name: 'Bulbasaur',
        frase: 'Olá, seu pokémon é o Bulbasaur, o tipo dele é Grama e a habilidade principal dele é Raio Solar'
      },
      {
        name: 'Charmander',
        frase: 'Olá, seu pokémon é o Charmander, o tipo dele é Fogo e a habilidade principal dele é Lança Chamas'
      },
      {
        name: 'Squirtle',
        frase: 'Olá, seu pokémon é o Squirtle, o tipo dele é Água e a habilidade principal dele é Jato de Água'
      },
    ];
    pokemonsListados.forEach((pokemon) => {
      getPokemonDetails(pokemon.name, (error, message) => { // chama a função com cada pokemon listado.
        try {
          expect(message).toBe(pokemon.frase); // para cada pokemon listado verifica se a saída é a respectiva frase do pokemon.
          done();
        } catch (error) {
          done(error)
        }
      });
    });
  });
});
