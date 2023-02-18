//Código da questão 5.
const messageDelay = () => Math.floor(Math.random() * 5000);

const getMarsTemperature = () => {
  const maxTemperature = 58;
  return Math.floor(Math.random() * maxTemperature);
};

const toFahrenheit = (degreeCelsius) => Math.floor((degreeCelsius * (9 / 5)) + 32);

const temperatureInFahrenheit = (temperature) =>
  console.log(`Atualmente está ${toFahrenheit(temperature)}ºF em Marte`);

const greet = (temperature) =>
console.log(`Olá! Curiosity aqui. Nesse momento está ${temperature}ºC em Marte`);

  // Meu código:
const sendMarsTemperature = (callBack) => {
    setTimeout(() => {
        const temperaturaAtual = getMarsTemperature()
        callBack(temperaturaAtual);
    }, messageDelay());
};

sendMarsTemperature(temperatureInFahrenheit);
sendMarsTemperature(greet);