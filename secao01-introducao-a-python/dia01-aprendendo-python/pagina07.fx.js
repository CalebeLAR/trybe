const Pagina06 = require('./pagina06.fx');

class Pagina07 extends Pagina06 {
  static ParaFixarIII = {
    Exercício12(){console.log(`
RESP:
>>> fat = 1;
>>> for numero in range(1,6):
...     fat *= numero
...     print(fat)
... 
1
2
6
24
120
    `)},
    Exercício13(){console.log(`
RESP:
  >>> ratings = [6,8,5,9,10]
  >>> ratings = [rate * 10 for rate in ratings]
  >>> ratings
  [60, 80, 50, 90, 100]
    `)},
    Exercício14(){console.log(`
RESP:
>>> ratings = [6,8,5,9,10]
>>> ratings = [rate for rate in ratings if ((rate % 3) == 0)]
>>> ratings
[6, 9]
    `)},
  }
}

Pagina07.ParaFixarIII.Exercício12();

