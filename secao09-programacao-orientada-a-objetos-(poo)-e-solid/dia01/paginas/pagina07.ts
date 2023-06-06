// // Encapsulamento

class Person07 {
  name: string;
  private _weight: number;
  private _age: number;
  readonly height: number;
  private _teste?: string;

  constructor(name: string, height: number, weight: number, age: number, teste?: string) {
    this.name = name;
    this._weight = weight;
    this._age = age;
    this.height = height;
    this._teste = teste;
  }

  getWeight() {
    // esta sintaxe permite acessar o valor retornado via person.getWeight()
      return this._weight;
  }

  get age() {
    // esta sintaxe permite acessar o valor retornado via person.age (como se fosse um atributo normal)
      return this._age;
  }
  set age(newValue: number) {
    // do mesmo modo, esta sintaxe permite modificar o valor com uma simples atribuição: person.age = 42
    // mesmo que esteja ocorrendo uma validação internamente
      if (newValue >= 0 && newValue < 200) {
        this._age = newValue;
    }
  }
  get teste () {
   return (this._teste ) || 'string';
  };

  set teste (newValue: string) {
    if (newValue === 'reset') {
      this._teste = `VALOR DE _teste RESETADO!`
    }
  }
  birthday() {
      this._age += 1;
  }
}
const _p1 = new Person07('Maria', 171, 58, 19);
const _p2 = new Person07('João', 175, 66, 18, 'init');
// Vamos agora a um exemplo de sintaxes que são válidas neste contexto:
// Alteração direta de variável pública
_p1.name = 'Mariah';
// Acesso direto a variável pública
console.log(_p1.name);
// Acesso a método público que manipula atributo privado
console.log(_p1.getWeight());
// Acesso a método com getter para manipular atributo privado como se fosse público
console.log(_p2.age);
// Acesso a método público que manipula atributo privado
_p2.birthday();
console.log(_p2.age);
// Acesso a método com setter para manipular atributo privado como se fosse público
_p2.age = 17;
console.log(_p2.age);
// Leitura de atributo readonly
console.log(_p1.height);
_p2.age = 300;
_p2.teste = 'reset'
console.log(_p2.age);
console.log(_p2.teste);