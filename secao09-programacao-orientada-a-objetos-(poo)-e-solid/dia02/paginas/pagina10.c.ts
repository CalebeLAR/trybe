const pagina10 = () => {
  // -----------------------
  //  Composição e Agregação
  // -----------------------
  const classeProfile = () => {
    //Anota aí 🖊: A composição de objetos/classes é uma forma de combinar objetos ou tipos de dados para construir sua estrutura.
    class Profile {
      private name: string = '';
      private email: string = '';

      public setName(name: string) {
        this.name = name;
      }

      public setEmail(email: string) {
        this.email = email;
      }

      public toString(): string {
        return `name - [${this.name}] - email - [${this.email}]`;
      }
    }

    class SocialMediaAccount {
      // Cria nossa composição com o perfil
      private profile = new Profile();

      public editProfile(name: string, email: string) {
        this.profile.setName(name);
        this.profile.setEmail(email);
      }

      public printProfile() {
        console.log(this.profile.toString());
      }
    }

    const socialMediaAccount = new SocialMediaAccount();
    socialMediaAccount.editProfile('Manuella', 'manu@trybe.com');
    socialMediaAccount.printProfile();
  }

  // ---------
  // Agregação
  // ---------
  const classeFriend = () => {
    class Friend {
      private nickname: string = '';

      public getNickname(): string {
        return this.nickname;
      }

      public setNickname(nickname: string) {
        this.nickname = nickname;
      }
    }

    class SocialMediaAccount {
      private friends = new Array<Friend>();

      public addFriend(friend: Friend) {
        this.friends.push(friend);
      }

      public printFriends() {
        this.friends.map((friend) => console.log(friend));
      }
    }

    const socialMediaAccount = new SocialMediaAccount();

    const friendCarol = new Friend();
    friendCarol.setNickname('Carol');

    const friendFernando = new Friend();
    friendFernando.setNickname('Fernando');

    socialMediaAccount.addFriend(friendCarol);
    socialMediaAccount.addFriend(friendFernando);
    socialMediaAccount.printFriends();
  }

  classeProfile();
  classeFriend();
};

pagina10();