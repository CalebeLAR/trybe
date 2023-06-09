const pagiana05_exer = () => {
  const paraFixarI = () => {
    // Para fixar:
    // Que tal exercitar a sintaxe um pouco, com um breve exercício bem simples? Juro que parece muita coisa, mas não é!
    //     Crie uma classe chamada Superclass.
    //     A Superclass deve possuir um atributo público isSuper
    //     isSuper deve ser setado como true na inicialização.
    //     A Superclass deve possuir um método público chamado sayHello, que deve imprimir “Olá mundo!”.
    //     Crie uma classe chamada Subclass que herda da Superclass.
    //     Crie uma função myFunc fora do escopo da Subclass que recebe um objeto da Superclass.
    //     Dentro dessa função, chame o método sayHello do objeto passado como parâmetro.
    //     Crie um objeto da Superclass e outro da Subclass.
    //     Chame a função myFunc 2 vezes, passando os objetos criados.


    class Superclass {
      public isSuper: boolean
      constructor() {
        this.isSuper = true;
      };
      sayHello() {
        console.log('Olá mundo!');
      }
    };

    class Subclass extends Superclass { };

    const myFunc = (cls: Superclass) => {
      cls.sayHello();
    }

    const superObj = new Superclass();
    const subObj = new Subclass()

    myFunc(superObj);
    myFunc(subObj);
  }

  const paraFixarII = () => {
    // Para fixar:
    // Com base no exemplo do exercício anterior:
    //     Comente a criação da instância da Superclass.
    //     Comente a chamada da função que recebe o objeto do tipo Superclass como argumento.
    //     Faça a função receber não mais um objeto da Superclass, mas sim da Subclass.
    //     Crie, na Subclass, um método público chamado sayHello2.
    //     Chame o método sayHello dentro do método sayHello2.
    //     Mude a visibilidade do método sayHello de public para protected.
    //     Ao mudar a visibilidade, o compilador (ou o vs code) vai mostrar um erro. Conserte esse erro utilizando o novo método sayHello2.
    //     Mude a visibilidade do método sayHello de protected para private. O que acontece?
    //        Resp: o codigo quebra pois a chamada this.sayHello na Subclass deixa de ser possível.
    //     Obs: Desfaça estas alterações antes de fazer o próximo exercício, ou seja, deixe como estava ao final do primeiro exercício.

    class Superclass {
      public isSuper: boolean
      constructor() {
        this.isSuper = true;
      };

      protected sayHello() {
        console.log('Olá mundo!');
      }
    };

    class Subclass extends Superclass {
      sayHello2() {
        this.sayHello();
      }
    };

    const myFunc = (cls: Subclass) => {
      // cls.sayHello(); // so pode ser chamado dentro de classes filhas!!
      cls.sayHello2();
    }

    // const superObj = new Superclass();
    const subObj = new Subclass()

    // myFunc(superObj);
    myFunc(subObj);
  }

  const paraFixarIII = () => {
    // Para fixar:
    // Com base no final do primeiro exercício de fixação:
    //     No construtor da Subclass, o atributo isSuper deve ser setado como false. Você vai precisar utilizar o super.
    //     Dentro da função que recebe um objeto da Superclass como parâmetro, cheque o valor do atributo isSuper e imprima no console “Super!” se for true e “Sub!” se for false;

    class Superclass {
      public isSuper: boolean
      constructor() {
        this.isSuper = true;
      };
      sayHello() {
        console.log('Olá mundo!');
      }
    };

    class Subclass extends Superclass {
      constructor() {
        super()
        super.isSuper = true;
      }
    };

    const myFunc = (cls: Superclass) => {
      cls.sayHello();
      console.log(cls.isSuper ? "Super" : "False");
    }

    const superObj = new Superclass();
    const subObj = new Subclass()

    myFunc(superObj);
    myFunc(subObj);
  }

  paraFixarI();
  paraFixarII();
  paraFixarIII();
};

pagiana05_exer();