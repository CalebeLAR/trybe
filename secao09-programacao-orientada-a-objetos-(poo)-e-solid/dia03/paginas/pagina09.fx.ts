const pagina09_exer = () => {
  const paraFixarI = () => {
    // Para fixar
    // Utilize a estrutura a seguir nos exercícios dessa seção:
    interface Character {
      name: string;
      specialMove: string;
    }

    interface DbCharacter extends Character {
      id: number;
    }

    const db: DbCharacter[] = [{name: 'test', specialMove: 'test', id: 1000}];
    //     Character define os atributos básicos de um personagem de um videogame de luta, com o nome do personagem (name) e de seu movimento especial (specialMove):
    //     DbCharacter estende os atributos da classe Character para incluir aqueles existentes no banco de dados.

    //     1 - Crie uma interface chamada IModel que defina as operações básicas de um CRUD para a entidade Character.
    interface IModel {
      create(character: Character):Promise<DbCharacter>;
      update(id: number, character: Character):Promise<DbCharacter|null>;
      delete(id: number):Promise<boolean|null>;
      getAll():Promise<DbCharacter[]>;
      getById(id: number):(Promise<DbCharacter|null>);
    }

    // 2 - Crie uma classe LocalDbModel que implemente a interface IModel.
    class LocalDbModel implements IModel {
      async create(character: Character): Promise<DbCharacter> {
        const  id = (!db.length)? 0: db.reduce((acc, curr)=> acc.id > curr.id ? acc: curr).id++;
        db.push({...character, id })

        return {...character, id };
      }
      
      async update(id: number, character: Character): Promise<DbCharacter|null> {
        if(!db.map(c => c.id).includes(id)) return null;

        const index = db.map(c=>c.id).indexOf(id);
        db.splice(index, 1, {...character, id});

        return db.find((c)=>c.id === id) || null;
      }

      async delete(id: number): Promise<boolean|null> {
        if(!db.map(c => c.id).includes(id)) return null;

        const index = db.map(c=>c.id).indexOf(id);
        db.splice(index,1);

        return !db.map(c=>c.id).includes(id);
      }
      async getAll(): Promise<DbCharacter[]> {

        return db
      }
      async getById(id: number): Promise<DbCharacter|null> {
        
        return db.find((c)=>c.id === id) || null;
      }  
    }

    // 3 - Crie uma classe CharacterService que recebe como dependência em seu construtor uma instância do tipo LocalDbModel e a utilize em sua lógica de negócio.
    class CharacterService {
      constructor(private localModel:LocalDbModel){}
      async create(character: Character) {
        const response = await this.localModel.create(character);

        return {status: 201, message: response}
      }
      async update(id: number, character: Character) {
        const response = await this.localModel.update(id, character);
        if (!response) return {status: 404, message: 'not found'};

        return {status: 201, message: response}
      }
      async delete(id: number) {
        const response = await this.localModel.delete(id);
        if (!response) return {status: 404, message: 'not found'};

        return {status: 201, message: response};
      }
      async getAll() {
        const response = await this.localModel.getAll();

        return {status: 201, message: response};
      }

      async getById(id: number) {
        const response = await this.localModel.delete(id);
        if (!response) return {status: 404, message: 'not found'};

        return {status: 201, message: response}
      }
    }


    // 4 - Refatore CharacterService para que possa receber uma instância de qualquer classe que implemente a interface IModel.

    class GenericService {
      constructor(private localModel:IModel){}

      async create(character: Character) {
        const response = await this.localModel.create(character);

        return {status: 201, message: response}
      }
      async update(id: number, character: Character) {
        const response = await this.localModel.update(id, character);
        if (!response) return {status: 404, message: 'not found'};

        return {status: 201, message: response}
      }
      async delete(id: number) {
        const response = await this.localModel.delete(id);
        if (!response) return {status: 404, message: 'not found'};

        return {status: 201, message: response}

      
      }
      async getAll() {
        const response = await this.localModel.getAll();

        return {status: 200, message: response};
      }

      async getById(id: number) {
        const response = await this.localModel.delete(id);
        if (!response) return {status: 404, message: 'not found'};

        return {status: 200, message: response}
      }
    }

    //5 - Crie uma classe MockedDbModel que implemente IModel com uma versão mock.
    class MockedDbModel implements IModel {
      async create(character: Character){
        console.log('character created');

        return {...character, id:1000 }
      }
      async update(id: number, character: Character) {
        console.log('character updadted');

        return {...character, id }
      }
      async delete(id: number){
        console.log('character deleted');

        return true;
      }
      async getAll() {
        return [
          {name:'test', specialMove:'teste', id: 1},
          {name:'test', specialMove:'teste', id: 2},
        ]
      }
      async getById(id: number) {
        return {name:'test', specialMove:'teste', id: 2}
      }

    }

    // 6 - Verifique que a classe CharacterService pode receber uma instância tanto de LocalDbModel como de MockedDbModel.
    
    const localDbModel = new LocalDbModel();
    const mockedDbModel = new MockedDbModel();
    const localCharacterService = new CharacterService(localDbModel);
    const mockCharacterService = new CharacterService(mockedDbModel);

    const test = async () => {
      await localCharacterService.create({name: 'açsdfasd', specialMove: '2'});
      await localCharacterService.create({name: 'açsdfasd', specialMove: '3'});
      await localCharacterService.create({name: 'açsdfasd', specialMove: 'fasd'});
      await localCharacterService.create({name: 'açsdfasd', specialMove: '6'});
      await localCharacterService.update(1002, {name: '1002', specialMove: '1002'});
      await localCharacterService.delete(1001);
      const r = await localCharacterService.getAll();
      console.log(r);

      mockCharacterService.create({name:'asfdd', specialMove:'asdf'})
    }

    test();
  }

  paraFixarI();
};

pagina09_exer();