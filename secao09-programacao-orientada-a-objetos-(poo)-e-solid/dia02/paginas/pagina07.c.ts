const pagina07 = () => {
  // ------------------------------
  // Como implementar uma Interface
  // ------------------------------
  const comoImplementarUmaInterface = () => {

    interface Animal {
      name: string;
      age: number;

      getBirthDate(): Date;
    }

    class Bird implements Animal {
      constructor(
        public name: string,
        private birthDate: Date) { }

      get age():number {
        var timeDiff = Math.abs(Date.now() - new Date(this.birthDate).getTime());
        return Math.floor(timeDiff / (1000 * 3600 * 24) / 365.25);
      }

      getBirthDate() { return this.birthDate; }

      fly() { console.log(`${this.name} está voando!`); }
    }

    const parrot = new Bird(
      'Papagaio',
      new Date(Date.parse('Aug 16, 2015')),
    );

    console.log(parrot.age);
    parrot.fly();
  }

  comoImplementarUmaInterface();
}

pagina07();