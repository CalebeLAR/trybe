const fs = require('fs').promises;

async function writeFile () {
  try {
    await fs.writeFile('./meuArquivo3.txt', '#titúlo \nquebra de linha',); // wx
    console.log('meu escrito lido com sucesso!');
  } catch (e) {
    console.error(`ERRO: ${e.message}`);
  }
};

writeFile();