const names = ['João', 'Irene', 'Fernando', 'Maria'];

const findNameWithFiveLetters = () => {
    const retorno = names.find((name) => (name.length === 50));
    return (!!retorno) ? retorno : "não encontrado!"
}

console.log(findNameWithFiveLetters());