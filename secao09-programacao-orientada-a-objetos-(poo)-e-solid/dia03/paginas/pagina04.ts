const pagina04 = () => {
//--------------------------------------
//           Polimorfismo
//--------------------------------------


class Animals {
    declare turns: number;
    public makeSound(sound: string) {
        console.log('Som emitido:' + sound, this.turns);
  }
}
class Dogs extends Animals {
    numberTurn(turns: number) {
        return turns;
  }
  makeSound( sound: string): void {
      const times = this.numberTurn(5);
      console.log(`Som emitido: ${sound}, ${times} vezes`);
  }
}
class Birds extends Animals {
    declare specie: string;
    makeSound (sound: string) {
      this.specie = 'pássaro';
      console.log(`O som emitido pelo ${this.specie} é ${sound}`);
  }
}
const dogs = new Dogs();
dogs.makeSound("au au au");
const birds = new Birds();
birds.makeSound("fiu fiu fiu fiu fiu");

// a sobre  escrita de metodos é feita sobrescrevendo a implementação da classe filha sobre a extendida pai.
};
pagina04();