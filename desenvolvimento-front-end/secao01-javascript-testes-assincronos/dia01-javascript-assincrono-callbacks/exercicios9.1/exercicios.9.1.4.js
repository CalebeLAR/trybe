//Código da questão 4.
const messageDelay = () => Math.floor(Math.random() * 5000);

const getMarsTemperature = () => {
  const maxTemperature = 58;
  return Math.floor(Math.random() * maxTemperature);
};

const sendMarsTemperature = () => {
    setTimeout(() => {
        const temperaturaAtual = getMarsTemperature()
        const mensagem = `A temperatura de Marte é: ${temperaturaAtual}C°`
        console.log(mensagem);
    }, messageDelay());
};

sendMarsTemperature();