const pagina08 = () => {
  // -------------------------
  // Sintaxe de encapsulamento
  // -------------------------

  // Vamos a um exemplo com código, para reforçar os aprendizados?

  class Person {
    name: string;
    private _weight: number;
    private _age: number;
    readonly height: number;

    constructor(name: string, height: number, weight: number, age: number) {
      this.name = name;
      this._weight = weight;
      this._age = age;
      this.height = height;
    }

  // esta sintaxe permite acessar o valor retornado via person.getWeight()
    getWeight() {
      return this._weight;
    }

  // // esta sintaxe permite acessar o valor retornado via person.age (como se fosse um atributo normal)
    get age() {
      return this._age;
    }

  // do mesmo modo, esta sintaxe permite modificar o valor com uma simples atribuição: person.age = 42
  // mesmo que esteja ocorrendo uma validação internamente
    set age(newValue: number) {
      if (newValue >= 0 && newValue < 200) {
        this._age = newValue;
      }
    }

    birthday() {
      this._age += 1;
    }

  }

  const p1 = new Person('Maria', 171, 58, 19);
  const p2 = new Person('João', 175, 66, 18);
  // Vamos agora a um exemplo de sintaxes que são válidas neste contexto:

  // Copiar
  // Alteração direta de variável pública
  p1.name = 'Mariah';
  // Acesso direto a variável pública
  console.log(p1.name);
  // Acesso a método público que manipula atributo privado
  console.log(p1.getWeight());
  // Acesso a método com getter para manipular atributo privado como se fosse público
  console.log(p2.age);
  // Acesso a método público que manipula atributo privado
  p2.birthday();
  console.log(p2.age);
  // Acesso a método com setter para manipular atributo privado como se fosse público
  p2.age = 17;
  console.log(p2.age);
  // Leitura de atributo readonly
  console.log(p1.height);

  p2.age = 300;
  console.log(p2.age);

  // Para Fixar
  // Utilizando o mesmo código dos exercícios de fixação anteriores:
  class _TV {
     // 5 - Altere a visibilidade dos atributos definidos na classe Tv para private.
    private _brand: string;
    private _size: number;
    private _resolution: string;
    private _connections: string[];
    private _connectedTo?: string;
    
    constructor (b:string,s:number,r:string,cs:string[]) {
      this._brand = b;
      this._size = s;
      this._resolution = r;
      this._connections = cs;
      this._connectedTo = undefined;
    };
  
    // 6 - Crie um método getter e um setter para o atributo _connectedTo, da classe Tv.
    get connectedTo () {
      if (this._connectedTo) {
        return this._connectedTo;
      }
      return 'anoter connectedTo'
    }
  
    set connectedTo (connection:string) {
  //     O setter deverá verificar se o valor definido está entre as conexões disponíveis (_connections) e:
  //         Em caso positivo, definir este valor para o atributo _connectedTo;
  //         Em caso negativo, imprimir no console a mensagem “Sorry, connection unavailable!”
  
      if (this._connections.includes(connection)) {
        this._connectedTo = connection;
      } else {
        console.log(`Sorry, ${connection} unavailable!`)
      }
    }
  
  
    turnOn() {
      console.log(`
        brand ${this._brand}
        size ${this._size}
        resulution ${this._resolution}
        connections ${this._connections}
        connectedTo ${this._connectedTo}
      `)
    }
  }

}

pagina08();