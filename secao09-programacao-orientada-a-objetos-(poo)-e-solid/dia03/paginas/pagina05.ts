//--------------------------------------
//        Sintaxe com classes
//--------------------------------------
const pagina05 = () => {
  // Sobrescrita de método
  const codigo01 = () => {
    class Animal {
      constructor(public name: string) { }
      move() { console.log(`${this.name} está se movendo.`); }
    }
    class Bird extends Animal {
      move() { console.log(`${this.name} está voando.`); }
    }
    class Mammal extends Animal {
      move() { console.log(`${this.name} está andando.`); }
    }
    const a = new Animal('Tubarão');
    const b = new Bird('Papagaio');
    const m = new Mammal('Tatu');
    const myMove = (animal: Animal) => {
      animal.move();
    }
    myMove(a);
    myMove(b);
    myMove(m);
  };

  const codigo02 = () => {
    class Animal {
      constructor(public name: string, private _dec01?:string) { }
      move() { console.log(`${this.name} está se movendo.`); }
      get dec01 () {
        return this._dec01;
      }
    }
    class Bird extends Animal {
      move() {
        super.move();
        console.log(`${this.name} está voando.`);
      }
    }
    class Mammal extends Animal {
      move() { console.log(`${this.name} está andando.`); }
    }

    class Dec extends Animal {
      move() { console.log(`${super.dec01} está andando.`); }
    }
    const a = new Animal('Tubarão');
    const b = new Bird('Papagaio');
    const m = new Mammal('Tatu');
    const d = new Mammal('dec', 'dexl');
    const myMove = (animal: Animal) => {
      animal.move();
    }
    myMove(a);
    myMove(b);
    myMove(m);
    myMove(d);

  }

  codigo01();
  codigo02();
};

pagina05();