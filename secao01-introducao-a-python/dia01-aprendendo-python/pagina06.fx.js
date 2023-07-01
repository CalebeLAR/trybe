const Pagina05 = require("./pagina05.fx");

class Pagina06 extends Pagina05{
  static ParaFixarII = {
    // Copie a lista abaixo para realizarmos os exercícios de fixação 5 e 6:
    // trybe_course = ["Introdução", "Front-end", "Back-end"]
    Exercício5() { console.log(`
      RESP:
      >>> trybe_course = ["Introdução", "Front-end", "Back-end"]
      >>> trybe_course.append("Ciência da Computação")
      >>> trybe_course
      ['Introdução', 'Front-end', 'Back-end', 'Ciência da Computação']
    `)},
    Exercício6() { console.log(`
      RESP:
      >>> trybe_course[0] = "Fundamentos"
      >>> trybe_course
      ['Fundamentos', 'Front-end', 'Back-end', 'Ciência da Computação']
    `)},
    Exercício7() { console.log(`
      RESP:
      >>> names = set()
      >>> names
      set()
      >>> help(names)
      >>> names.add('calebe')
      >>> names
      {'calebe'}
    `)},
    Exercício8() { console.log(`
    RESP:
      >>> info
      {'personagem': 'Margarida', 'origem': 'Pato Donald', 'nota': 'Namorada do personagem principal nos quadrinhos do Pato Donald'}
      >>> info["recorrente"] = "Sim"
      >>> info
      {'personagem': 'Margarida', 'origem': 'Pato Donald', 'nota': 'Namorada do personagem principal nos quadrinhos do Pato Donald', 'recorrente': 'Sim'}
    `)},
    Exercício9() { console.log(`
      RESP:
      >>> del info["origem"];
      >>> info
      {'personagem': 'Margarida', 'nota': 'Namorada do personagem principal nos quadrinhos do Pato Donald', 'recorrente': 'Sim'}
    `)},
    Exercício10() { console.log(`
      RESP: TUPLA
    `)},
    Exercício11() { console.log(`
      RESP: LISTA
    `)}
  }
}

module.exports = Pagina06;