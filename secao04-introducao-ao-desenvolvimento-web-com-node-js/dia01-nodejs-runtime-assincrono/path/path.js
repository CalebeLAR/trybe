const path = require('path');
console.log(path.dirname('/usr/shere/gnome'))
console.log(path.resolve('usr','shere','gnome'))
console.log(path.resolve('/', 'usr','shere','gnome'))
console.log(path.resolve(__dirname))
console.log(path.resolve(__filename))