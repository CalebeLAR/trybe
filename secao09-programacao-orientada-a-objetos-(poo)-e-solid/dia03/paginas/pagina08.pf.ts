/**
  -----------------------------
  Métodos e atributos estáticos
  -----------------------------
**/

const pagina08 = () => {
  class Employee {
    /* Atributo estático, que pertence a classe */
    private static employeeCount = 0

    /* Aqui temos o exemplo de um atributo comum que, em contraste com o atributo estático,
    é utilizado pelas instâncias e não pela classe */
    private employeeName: string;

    constructor(name: string) {
      /* Pelo fato do o método addEmployee() ser estático, ou seja, acessível 
      apenas a partir da própria classe e não de suas instâncias, é que a
      chamamos a partir de Employee e não do 'this' */
      Employee.addEmployee();

      // Nesse caso, o 'this' se refere à instância dessa classe, que está sendo construída
      this.employeeName = name;
    }

    // Esse é um método exclusivo da classe, por isso estático 
    private static addEmployee() {
      /* Nesse caso, como o atributo é estático, melhor forma de acessar
      o atributo é a partir do nome da classe.  */
      Employee.employeeCount += 1;
      console.log(`Total de pessoas funcionárias: ${Employee.employeeCount}`)
    }

    /* Aqui temos o exemplo de método comum que, em contraste com o método estático,
    é utilizado pelas instâncias e não pela classe */
    public getName(): string {
      // Novamente, o 'this' se referindo à instância
      return this.employeeName
    }
  }

  const employee1 = new Employee('Kissyla'); // Total de pessoas funcionárias: 1
  const employee2 = new Employee('Calaça'); // Total de pessoas funcionárias: 2
  const employee3 = new Employee('Setinha'); // Total de pessoas funcionárias: 3

  const parafixar02 = () => {
    // 1 - Continuando com o exercício anterior do jogo de luta Super Smash Bros, vamos aplicar uma refatoração com base no conteúdo acima. Crie um método estático que receba como parâmetro character: Character e, dentro dele, chame os métodos talk e specialMove para apresentar o personagem.

    abstract class Character {
      abstract talk(): void;
      abstract specialMove(): void;

      static _count:number = 0;
      static characterPresentation(character: Character): void {
        character.talk();
        character.specialMove();
        console.log(Character._count);
      }
      constructor(){
        Character._count += 1;
      }

      get count () {
        return Character._count;
      }
    }

    class MeleeCharacter extends Character {
      constructor(private name:string, private especial:string) {
        super();
      }
      talk(): void {
        console.log(`${this.name}: está correndo`, super.count);
      };
      specialMove(): void {
        console.log(`${this.name} está usando: ${this.especial}`);
      };
    }

    class LongRangerCharacter extends Character {
      constructor(private name:string, private especial:string) {
        super();
      }
      talk(): void {
        console.log(`${this.name}: está correndo`);
      };
      specialMove(): void {
        console.log(`${this.name} está usando: ${this.especial}`);
      };
    }

    // 2 - Agora, ao invés de acionarmos os métodos talk e specialMove individualmente a partir das instâncias, acione-os por meio do método estático criado no exercício anterior.

    const yoshi = new MeleeCharacter('Yoshi', 'Super dragon');
    const samus = new LongRangerCharacter('Samus', 'Zero Laser');
    
    Character.characterPresentation(yoshi);
    Character.characterPresentation(samus);
  }
  parafixar02();
};
pagina08();