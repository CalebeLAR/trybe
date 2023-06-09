const pagina05 = () => {
  // |===============|
  // | Sintaxe geral |
  // |===============|
  const sintaxeGeral = () => {

    class Animal {
      constructor(public name: string, private birthDate: Date) { }

      get age() {
        const timeDiff = Math.abs(
          Date.now() -
          new Date(this.birthDate).getTime()
        );

        return Math.floor(timeDiff / (1000 * 3600 * 24) / 365.25);
      }
    }

    class Mammal extends Animal {
      walk() {
        console.log(`${this.name} está andando!`);
      }
    }

    const tiger = new Mammal(
      'Tigre',
      new Date(Date.parse('May 03, 2020')),
    );

    const main = (animal: Animal) => {
      console.log(animal.age);
    }

    main(tiger);
    tiger.walk();

    class Bird extends Animal {
      fly() {
        console.log(`${this.name} está voando!`);
      }
    }

    const parrot = new Bird(
      'Papagaio',
      new Date(Date.parse('Jun 07, 2017')),
    );

    console.log(parrot.age);
    parrot.fly();
  }

  // |===============================|
  // |Atributos protegidos(protected)|
  // |===============================|
  const atributosProtegidos = () => {
    const private = () => {
      class Animal {
        constructor(private birthDate: Date) { } // Repare no private

      }
      class Bird extends Animal {
        showBirthDate() {
          // console.log(this.birthDate); // ERRO! birthDate é privado e não é visível pra subclasse Bird.
        }
      }
    }

    const protected = () => {
      class Animal {
        protected birthDate: Date;
        public pub: string;
        constructor() {
          this.birthDate = new Date();
          this.pub = 'att pub';

        } // Protected: classe filha pode ler e escrever, mas acessos externos não
      }
      class Bird extends Animal {
        showBirthDate() {
          console.log(this.birthDate); // Okay!
          console.log(this.pub); // Okay!
        }
      }
    }


    private();
    protected();
  }

  // |=====|
  // |Super|
  // |=====|
  const _super = () => {
    const casoFalha = () => {
      class Animal {
        constructor(protected birthDate: Date) { }
      }
      class Bird extends Animal {
        // constructor(public name: string) { } // ERRO: constructor deve respeitar o contrato da superclasse
      }
    }

    const casoSucesso = () => {
      class Animal {
        constructor(protected birthDate: Date) { }
      }
      class Bird extends Animal {
        constructor(public name: string) {
          super(new Date()); // faz com que as instâncias de Bird recebam e definam os mesmos parâmetros que Animal e os definam como tal.
        }
      }

      casoFalha();
      casoSucesso();
    }
  };

  atributosProtegidos();
  sintaxeGeral();
  _super();
};

pagina05();