const fetch = require('node-fetch');

const anotações = {
    aula: "usando o async",
    //     const fecthConsultaCep = async (cep) => {
    //     try {
    //         const requisição = await fetch (`https://viacep.com.br/ws/${cep}/json/`);
    //         const resposta = await requisição.json();

    //         const { logradouro } = resposta;
    //         console.log(logradouro);

    //         return logradouro;
    //     } catch (error){
    //         return error.mensage;
    //     }
    // };
    primeiro: "a função async só funciona com o fatch",
    // const log = async () => {
    //     const resp = await consultaCep('30130010');
    //     console.log(await consultaCep('30130010'));
    // }
    sengundo: "a função fetch so funciona com URLs, não funciona com setTimeout"
    // const funAssinc = () => (setTimeout(()=>('responsta da função assíncrona'),3000));

    // const fatchCep = async (cep) => {
    //     const response = await fetch(funAssinc());
    //     console.log(response);
    // }
}

const consultaCep = async (cep) => {
    try {
        const requisição = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
        const resposta = await requisição.json();

        const { logradouro } = resposta;
        console.log(logradouro);

        return logradouro;
    } catch (error) {
        return error.mensage;
    }
};
// consultaCep("30130010");
module.exports = {consultaCep};