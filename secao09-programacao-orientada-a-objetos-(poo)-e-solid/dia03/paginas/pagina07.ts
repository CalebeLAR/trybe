/**
  --------------------------------------
  Classes, métodos e atributos abstratos
  -------------------------------------- 
 **/
const pagina07 = () => {
  abstract class Employee {
    constructor(public name: string) { }

    /* Aqui temos um atributo abstrato que implica às classes
    filhas atribuírem, de maneira obrigatória, um valor do tipo 'number' */
    declare MIN_SALARY: number

    /* Já aqui temos um método abstrato que implica às classes filhas 
    implementá-la, de maneira obrigatória, de acordo com a utilidade da classe filha  */
    abstract work(): void
  }

  class Instructor extends Employee {
    constructor(public name: string) {
      super(name);
    }
    MIN_SALARY = 10000;
    work() { console.log(`${this.name} está auxiliando as pessoas estudantes em mentorias.`); }
  }

  class Specialist extends Employee {
    constructor(public name: string) {
      super(name);
    }
    MIN_SALARY = 20000;
    work() { console.log(`${this.name} está ministrando uma aula ao vivo.`); }
  }

  class Facilitator extends Employee {
    constructor(public name: string) {
      super(name);
    }
    MIN_SALARY = 50000;
    work() { console.log(`${this.name} está conduzindo um 1:1.`); }
  }

  const instructor = new Instructor('Victor');
  const specialist = new Specialist('Gus');
  const facilitator = new Facilitator('Silvinha');

  instructor.work(); // Victor está auxiliando as pessoas estudantes em mentorias.
  specialist.work(); // Gus está ministrando uma Aula Ao Vivo.
  facilitator.work(); // Silvinha está conduzindo um 1:

  const parafixar01 = () => {
    // 1 - Crie uma classe abstrata Character que tenha os métodos abstratos talk(): void e specialMove(): void.
    abstract class Character {
      abstract talk(): void;
      abstract specialMove(): void;
    }
    // 2 - Crie a classe concreta MeleeCharacter que estenda Character e sobrescreva os métodos abstratos dessa classe.
    class MeleeCharacter extends Character {
      talk(): void {
        console.log('MeleeCharacter: está correndo');
      };
      specialMove(): void {
        console.log('MeleeCharacter: está correndo e dando soco em geral');
      };
    }

    // 3 - Crie a classe concreta LongRangeCharacter que estenda Character e sobrescreva os métodos abstratos dessa classe.
    class LongRangerCharacter extends Character {
      talk(): void {
        console.log('LongRangerCharacter: está correndo');
      };
      specialMove(): void {
        console.log('LongRangerCharacter: está correndo e dando tiro em geral');
      };
    }

    // 4 - Agora instancie as classes filhas com os personagens Yoshi e Samus, com seus respectivos specialMoveName e chame os métodos talk e specialMove para apresentar o personagem e seus respectivos ataques especiais.
    const Samus = new MeleeCharacter();
    const Yoshi = new LongRangerCharacter();
    [Samus, Yoshi].forEach((character:Character) => {
      character.specialMove();
      character.talk()
    })
  }
  parafixar01();
};
pagina07();