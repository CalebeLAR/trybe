const fs = require('fs');

const data = fs.readFileSync('secao04-introducao-ao-desenvolvimento-web-com-node-js/dia01-nodejs-runtime-assincrono/modulos-internos/meuarquivo.txt');
console.log(data.toString())