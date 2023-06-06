// Sintaxe geral
// Agora, vamos ver como fica a sintaxe de criação de classes, objetos, atributos e métodos em TypeScript. Para isso vamos utilizar o exemplo visto anteriormente:
class Person {
  name: string;
  height: number;
  weight?: number; // o caractere "?" indica um atributo opcional
  constructor(n: string, h: number, w?: number) {
      console.log(`Creating person ${n}`);
    this.name = n;
    this.height = h;
    this.weight = w;
  }
  sleep() {
      console.log(`${this.name}: zzzzzzz`);
  }
}
const p1 = new Person('Maria', 171, 58);
const p2 = new Person('João', 175);
console.log(p1.name, p1.height, p1.weight);
console.log(p2.name, p2.height, p2.weight);
p1.sleep();
p2.sleep();
// Para Fixar
// Utilizando o que você já aprendeu até aqui, faça o seguinte exercício:
// 1 - Crie uma classe chamada Tv, com os atributos:
//     brand: marca da TV;
//     size: tamanho em polegadas;
//     resolution: resolução da tela;
//     connections: conexões disponíveis(HDMI, Ethernet, etc.);
//     connectedTo: conexão atual Este atributo não precisa ser inicializado no construtor.
class TV {
  brand: string;
  size: string;
  resolution: string;
  connections: string[];
  connectedTo?: string;

  constructor (b:string,s:string,r:string,cs:string[],co?:string) {
    this.brand = b;
    this.size = s;
    this.resolution = r;
    this.connections = cs;
    this.connectedTo = co;
  };

  // 2 - Dentro da classe Tv, crie o método turnOn, que imprimirá os atributos inicializados no construtor.
  turnOn() {
    console.log(`
      brand ${this.brand}
      size ${this.size}
      resulution ${this.resolution}
      connections ${this.connections}
      connectedTo ${this.connectedTo}
    `)
  }
}
// 3 - Instancie um objeto a partir da classe Tv, chame o método turnOn para imprimir seus atributos.
const TV1 = new TV('samsumg', '40p', '4K', ['internet', 'cabo', 'radio', 'sinal-fumaça']);

TV1.turnOn();
