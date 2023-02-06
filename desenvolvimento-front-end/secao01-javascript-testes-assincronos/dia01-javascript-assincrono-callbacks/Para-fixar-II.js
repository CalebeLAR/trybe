const userFullName = ({ firstName, lastName }) => `Hello! My name is ${firstName} ${lastName}`;
const userNationality = ({ firstName, nationality }) => `${firstName} is ${nationality}`;

const delay = (maxMilliseconds = 1000) => Math.floor(Math.random() * maxMilliseconds);

const getUser = (callback) => {

    setTimeout(() => {
    const didOperationSucceed = Math.random() >= 0.5;
    console.log(didOperationSucceed);
    if (didOperationSucceed) {
    const user = {
      firstName: "Ivan",
      lastName: "Ivanovich",
      nationality: "Russian",
      }
      console.log(callback(user));
    } else {
      // Retorne a `callback` passada como parâmetro na função `getUser`
      console.log(user);
    }
    
    // Dica: você pode manter o `console.log()`
    // return callback(user);
  }, delay());
  // return (user)

};

console.log(getUser(userFullName)); // deve imprimir "Hello! My name is Ivan Ivanovich" depois de um certo tempo
// getUser(userNationality); // deve imprimir "Ivan is Russian" depois de um certo tempo
