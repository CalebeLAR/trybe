//Código da questão 6.
const messageDelay = () => Math.floor(Math.random() * 5000);

const getMarsTemperature = () => {
  const maxTemperature = 58;
  return Math.floor(Math.random() * maxTemperature);
}

const toFahrenheit = (degreeCelsius) => Math.floor((degreeCelsius * (9 / 5)) + 32);

const temperatureInFahrenheit = (temperature) =>
  console.log(`It is currently ${toFahrenheit(temperature)}ºF at Mars`);

const greet = (temperature) =>
  console.log(`Hi there! Curiosity here. Right now is ${temperature}ºC at Mars`);

const handleError = (errorReason) =>
  console.log(`Error getting temperature: ${errorReason}`);

const responseStatus = () => {return Math.random() <= 0.6;
};

// Meu código:
  const sendMarsTemperature = (callBack, errorReason) => {
    setTimeout(() => {
        //Chama a callback: verifyMensage. Caso seja true, então chama a callBack;
        if (responseStatus()) {
            const temperaturaAtual = getMarsTemperature();
            callBack(temperaturaAtual);
        } else {
            errorReason("Robot is busy")
        }
    }, messageDelay());
};

sendMarsTemperature(temperatureInFahrenheit, handleError);
sendMarsTemperature(greet, handleError);

//verificando a porcentagem;
// let arr = [];
// for ( let i = 0; i <= 109999999; i += 1){
//     const boleans = Math.random() <= 0.6;
//     arr.push(boleans);
// };

// const trues = arr.filter((valores)=>(valores === true)).length;
// const falses = arr.filter((valores)=>(valores === false)).length;
// const porcentagemTrues  = Math.floor(100 * (trues/arr.length));
// const porcentagemFalses = Math.floor(100 * (falses/arr.length));
// console.log(`numero de trues: ${true}\nporcentagem: ${porcentagemTrues}\n`);
// console.log(`numero de falses: ${falses}\nporcentagem: ${porcentagemFalses}`);