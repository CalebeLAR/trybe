//----------------------------------------
// Classes, métodos e atributos abstratos
//----------------------------------------
const pagina06 = () => {
// Por vezes, criamos classes que devem possuir métodos pensados para serem implementados em subclasses.

// A ideia é que a superclasse, mais genérica, não deve fazer ideia de como esse método deve funcionar, apenas saber que ele existe.

// Isso é o mesmo que quando há uma implementação de interface, com a diferença na interface nenhum método é implementado, e aqui queremos selecionar alguns métodos para que não sejam implementados.

// Para isso, utilizamos classes abstratas, e estas possuem métodos abstratos.

// As classes abstratas não podem ser instanciadas, ou seja, você não pode criar um objeto a partir de uma classe abstrata.

// Métodos abstratos só podem existir em classes abstratas, e eles devem ser implementados na subclasse.

// No exemplo abaixo temos uma classe abstrata Employee que possui um atributo abstrato(MIN_SALARY) e um método abstrato (work()) que se aplica a seus subtipos. No caso da Trybe, temos pessoa instrutora, pessoa especialista e pessoa facilitadora. Portanto, ao criar as classes de cada subtipo, estendemos a partir da classe abstrata Employee e implementamos o atributo e o método de acordo com suas particularidades.

// /*

// Dicionário en-pt:

// - employee: pessoa empregada/funcionária

// */


// abstract class Employee {

//   constructor(public name: string) { }


//   /* Aqui temos um atributo abstrato que implica às classes

//   filhas atribuírem, de maneira obrigatória, um valor do tipo 'number' */

//   abstract MIN_SALARY: number


//   /* Já aqui temos um método abstrato que implica às classes filhas 

//   implementá-la, de maneira obrigatória, de acordo com a utilidade da classe filha  */

//   abstract work(): void

// }


// class Instructor extends Employee {

//   constructor(public name: string) {

//     super(name); 

//   }

//   MIN_SALARY = 10000;

//   work() { console.log(`${this.name} está auxiliando as pessoas estudantes em mentorias.`); }

// }


// class Specialist extends Employee {

//   constructor(public name: string) {

//     super(name); 

//   }

//   MIN_SALARY = 20000;

//   work() { console.log(`${this.name} está ministrando uma aula ao vivo.`); }

// }


// class Facilitator extends Employee {

//   constructor(public name: string) {

//     super(name); 

//   }

//   MIN_SALARY = 50000;

//   work() { console.log(`${this.name} está conduzindo um 1:1.`); }

// }


// const instructor = new Instructor('Victor');

// const specialist = new Specialist('Gus');

// const facilitator = new Facilitator('Silvinha');


// instructor.work(); // Victor está auxiliando as pessoas estudantes em mentorias.

// specialist.work(); // Gus está ministrando uma Aula Ao Vivo.

// facilitator.work(); // Silvinha está conduzindo um 1:1.

// Veja na prática como funcionam as classes abstratas:
// Para fixar

// Suponha que você está modelando os personagens do jogo de luta multijogadores Super Smash Bros. No jogo, há personagens de alcances variados e movimentos especiais variados. Vence a pessoa que acumulou mais pontos na partida.

// 1 - Crie uma classe abstrata Character que tenha os métodos abstratos talk(): void e specialMove(): void.

// 2 - Crie a classe concreta MeleeCharacter que estenda Character e sobrescreva os métodos abstratos dessa classe.

// 3 - Crie a classe concreta LongRangeCharacter que estenda Character e sobrescreva os métodos abstratos dessa classe.

// 4 - Agora instancie as classes filhas com os personagens Yoshi e Samus, com seus respectivos specialMoveName e chame os métodos talk e specialMove para apresentar o personagem e seus respectivos ataques especiais.
};