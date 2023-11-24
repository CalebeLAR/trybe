class Pagina05 {
  static ParaFixarI = {
    Exercício1() {console.log(`
      RESP:
      >>> a = 10 
      >>> b =5
      >>> soma = a + b
      >>> subtração = a - b
      >>> multiplicação = a * b
      >>> divisão = a / b
      >>> divisão_inteira = a // b
      >>> patenciação = a ** b
      >>> módulo = a % b
      >>> print('soma:', soma,'subtração:', subtração,'multiplicação:', multiplicação,'divisão:', divisão,'divisão_inteira:', divisão_inteira,'potenciação:', potenciação,'módulo:', módulo)
      soma: 15 subtração: 5 multiplicação: 50 divisão: 2.0 divisão_inteira: 2 potenciação: 100000 módulo: 0

    `)},
    Exercício2() {console.log(`
      RESP:
      >>> hours = 6
      >>> hours
      >>> mim = (hours * 6 * 60)
      >>> seg = (2160 * 60)
      >>> print(f'{hours}h tem {mim}min e {seg}s')
      6h tem 2160min e 129600s
    `)},
    Exercício3() {console.log(`
      RESP: executa sem erros
      >>> soma = 4 + 5;
      >>> soma
      9
    `)},
    Exercício4() {console.log(`
    RESP: 918.4499999999999
      >>> books = 60
      >>> book_price = (1 - 0.4) * 24.20
      >>> logistic = 3 + (books - 1) * 0.75
      >>> cost = books * book_price + logistic
      >>> cost
      918.4499999999999
    `)},
  }
}

module.exports = Pagina05;
