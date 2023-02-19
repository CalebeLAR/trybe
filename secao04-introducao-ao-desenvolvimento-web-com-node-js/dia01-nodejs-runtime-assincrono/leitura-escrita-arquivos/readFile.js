const fs = require('fs').promises;

async function main () {
  try {
    const data = await fs.readFile('./meuArquivo.txt', 'utf-8');
    console.log(data);
  } catch(script) {
    console.error(`saída to terminal:`);
    try {
      const data = await fs.readFile('secao04-introducao-ao-desenvolvimento-web-com-node-js/dia01-nodejs-runtime-assincrono/leitura-escrita-arquivos/meuArquivo.txt', 'utf-8');
      console.log(data)
    } catch (saida){
      console.error('não foi possivel mostrar na saída to terminal');
    }
  }
}

main();