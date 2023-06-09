const pagina10_exer = () => {
  const paraFixarI = () => {

    // Para fixar:
    // Crie uma interface Logger.
    // Logger deve possuir um método log, que recebe um parâmetro do tipo string e não retorna nada (void).
    // Crie uma classe ConsoleLogger que implementa Logger. Você deve imaginar como o método log deve ser implementado, né? 😁.
    interface Logger {
      log(param:string):void;
    }
    class ConsoleLogger implements Logger {
      log(param: string): void {
        console.log(`consolelogger(1) ${param}`);
      }
      
    }

    class ConsoleLogger2 implements Logger {
      log(param: string): void {
        console.log(`consolelogger(2) ${param}`);

      }
    }
    // Crie uma classe ConsoleLogger2 igual à classe anterior, apenas a título de exemplo.
    // No console.log dentro do método log, diferencie o ConsoleLogger2 do ConsoleLogger.
    // Crie uma interface Database.

    interface Database {
      logger: Logger;
      save(key:string, value:string):void;
    }
    // Database deve possuir um atributo do tipo Logger.
    // Database deve possuir um método save, que recebe dois parâmetros, key e value, ambos strings, e não retorna nada (void).
    // Crie uma classe ExampleDatabase que implementa Database.
    // ExampleDatabase deve receber o Logger como parâmetro do construtor, e possuir como valor padrão um ConsoleLogger.
    // Dentro do método save, chame a função log do Logger passado para o database para fazer o log dos parâmetros passados para a save.
    class ExampleDatabase implements Database {
      constructor(public logger:Logger=new ConsoleLogger()){}
      save(key: string, value: string): void {
        this.logger.log(`ExampleDatabase: ${key} ${value}`);
      }
      
    }
    // Crie um objeto de cada um dos Loggers.
    const logger1 = new ConsoleLogger();
    const logger2 = new ConsoleLogger2();
    // Crie três objetos da ExampleDatabase, cada um dos dois primeiros recebendo um dos Loggers, e o último não recebendo nenhum.
    const firstExampleDatabase = new ExampleDatabase(logger1);
    const secondExampleDatabase = new ExampleDatabase(logger2)
    const thirdExampleDatabase = new ExampleDatabase()
    // Utilize todos eles para salvar um conteúdo fictício.
    firstExampleDatabase.save('fkey', 'fvalue');
    secondExampleDatabase.save('skey', 'svalue');
    thirdExampleDatabase.save('tkey', 'tvalue');
  }
  paraFixarI();
}

pagina10_exer();