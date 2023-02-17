function createDaysOfTheWeek() {
    const weekDays = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    const weekDaysList = document.querySelector('.week-days');
  
    for (let index = 0; index < weekDays.length; index += 1) {
      const days = weekDays[index];
      const dayListItem = document.createElement('li');
      dayListItem.innerHTML = days;
  
      weekDaysList.appendChild(dayListItem);
    };
  };
  
  createDaysOfTheWeek();
  
  // Escreva seu código abaixo.
// 🚀 Exercício 1:
// Crie um calendário dinamicamente.
// O array decemberDaysList contém os dois últimos dias de novembro e os dias do mês de dezembro. Sua função deve criar dinamicamente cada dia do calendário e os adicionar dentro da tag <ul>.
// Note que os dias 29 e 30 de novembro estão no array, pois representam respectivamente Domingo e Segunda-feira.
// *A tag <ul> deve conter o id 'days';
// *Os dias devem estar contidos em uma tag <li>, e todos devem ter a classe day. Ex: <li class="day">3</li>
// *Os dias 24, 25 e 31 são feriados e, além da classe day, devem conter também a classe holiday. Ex: <li class="day holiday">24</li>
// *Os dias 4, 11, 18 e 25 são sextas-feiras. Eles devem conter a classe day e a classe friday. Ex: <li class="day friday">4</li>

let decemberDaysList = [29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31];
// let ul = document.createElement('ul');
// ul.id = "days";
function criaLis () {
    const ul_de_dias = document.getElementById('days');
    for (dia of decemberDaysList) {
        
        let li = document.createElement('li')
        li.innerHTML = dia;
        li.classList.add("day");

        // li.style.backgroundColor = 'blue'

        if (dia === 24 || dia === 25 || dia === 31){
            li.classList.add("holiday")
            
        }
        if (dia === 4 || dia === 11|| dia === 18 || dia === 25) {
            li.classList.add("friday");
        }
        
        ul_de_dias.appendChild(li);
    }      
}
criaLis()

    // 🚀 Exercício 2:
// Implemente uma função que crie dinamicamente um botão com o nome "Feriados".
// Sua função deve receber um parâmetro com a string 'Feriados'
// Adicione a este botão a ID "btn-holiday"
// Adicione este botão como filho/filha da tag <div> com classe "buttons-container"

let nomeBotão = 'feriados'
function botãoHoliday (nomeBotão){
    const div_buttons_container = document.querySelector('.buttons-container');

    let botão = document.createElement('button');
    botão.innerHTML = nomeBotão;
    botão.id = 'btn-holiday';
    
    div_buttons_container.appendChild(botão);
    //ex3
    botão.addEventListener("click", mudaCorHoliday)
}
botãoHoliday(nomeBotão)

// 🚀 Exercício 3:
// Implemente uma função que muda a cor de fundo dos dias que possuem a classe "holiday".
// Adicione ao botão "Feriados" um evento de "click" que altere a cor de fundo dos dias que possuem a classe "holiday"
// 👀 É interessante que esse botão possua também a lógica inversa. Ao ser clicado novamente, ele retorna à configuração inicial com a cor "rgb(238,238,238)".
function mudaCorHoliday(){
    const diasHoliday = document.querySelectorAll('.holiday');
    for ( let elemeto of diasHoliday) {
        let corAtual = elemeto.style.backgroundColor;
        
        if (corAtual === '') {
            elemeto.style.backgroundColor = 'rgb(60,159,113)';
            elemeto.style.border = '2px solid rgb(0,128,0)';
        } else {
            elemeto.style.backgroundColor = '';
            elemeto.style.border = '';
        }

    }

}

// 🚀 Exercício 5:
// Implemente uma função que modifica o texto exibido nos dias que são Sexta-feira. Adicione ao botão "Sexta-feira" um evento de "click" e modifique o texto a ser exibido nos dias que são sextas-feiras.
// 👀 É interessante que esse botão possua também a lógica inversa. Ao ser clicado novamente, ele retorna à configuração inicial exibindo os dias.

let Sexta_Feira = 'Sexta Feira';
function botãoSextaFeira (nomeBotão){
    const div_buttons_container = document.querySelector('.buttons-container');

    let botão = document.createElement('button');
    botão.innerHTML = nomeBotão;
    botão.id = 'btn-friday';
    
    div_buttons_container.appendChild(botão);
    // ex4
    botão.addEventListener('click', mudaCorSexta_Feira)
}

botãoSextaFeira(Sexta_Feira);

// 🚀 Exercício 5:
// Implemente uma função que modifica o texto exibido nos dias que são Sexta-feira. Adicione ao botão "Sexta-feira" mudaCorHolidayum evento de "click" e modifique o texto a ser exibido nos dias que são sextas-feiras.
// 👀 É interessante que esse botão possua também a lógica inversa. Ao ser clicado novamente, ele retorna à configuração inicial exibindo os dias.

function mudaCorSexta_Feira() {
    const diasHoliday = document.querySelectorAll('.friday');
    for ( let elemeto of diasHoliday) {
        let corAtual = elemeto.style.backgroundColor;
        if (corAtual === '') {
            elemeto.style.backgroundColor = 'rgb(0,100,0)'
            elemeto.style.border = '2px solid rgb(0,128,0)'
        } else {
            elemeto.style.backgroundColor = ''
            elemeto.style.border = ''
        }
    }

} 
// 🚀 Exercício 6:
// Implemente duas funções que criem um efeito de "zoom". Ao passar o ponteiro do mouse em um dia do mês no calendário, o texto desse dia deve aumentar e, quando o ponteiro do mouse sair do dia, o texto deve retornar ao tamanho original.
// Dica - Propriedade: event.target.
function addEventZoom () {
    function efeitoZoom (event) {
        event.target.style.fontSize = "25px";
        event.target.style.color = "rgb(0,191,255)";
    }
    function efeitoSmall (event) {
        event.target.style.fontSize = "20px";
        event.target.style.color = "rgb(119,119,119)";
    }
    const lis = document.querySelectorAll('.day');
    for (li of lis) {
        li.addEventListener('mouseover', efeitoZoom);
        li.addEventListener('mouseout', efeitoSmall);
    }
}
addEventZoom()
// 🚀 Exercício 7:
// Implemente uma função que adicione uma tarefa personalizada ao calendário. A função deve receber como parâmetro a string com o nome da tarefa (ex: "cozinhar") e criar dinamicamente um elemento com a tag <span> contendo a tarefa.
// O elemento criado deverá ser adicionado como filho/filha da tag <div> que possui a classe "my-tasks".
let input = "estudar para a trybe"
function tasks (string){
    const div_my_tesks = document.querySelector('.my-tasks');
    let span = document.createElement('span');
    span.innerText = string;
    div_my_tesks.appendChild(span);

}
tasks(input)
tasks("ler")

// 🚀 Exercício 8:
// Implemente uma função que adicione uma legenda com cor para a tarefa.
// * Essa função deverá receber como parâmetro uma string ('cor') e criar dinamicamente um elemento de tag `<div>` com a classe `task`.
// O parâmetro cor deverá ser utilizado como cor de fundo da <div> criada.
// O elemento criado deverá ser adicionado como filho/filha da tag <div> que possui a classe "my-tasks".
let cor = "rgb(60,179,113)"
function legendaTask (cor) {
    const div_my_tesks = document.querySelector('.my-tasks').children;
    for (let index = 1; index < div_my_tesks.length; index += 1) {
        console.log(div_my_tesks[index]);
        
        let div_task = document.createElement("div");
        div_task.classList.add('task');
        div_task.style.backgroundColor = cor;

        div_my_tesks[index].appendChild(div_task);       
    }
}
legendaTask(cor);

// 🚀 Exercício 9:
// Implemente uma função que selecione uma tarefa.
// Adicione um evento que ao clicar no elemento com a tag <div> referente à cor da sua tarefa, atribua a esse elemento a classe task selected, ou seja, quando sua tarefa possuir a classe task selected ela estará selecionada.
// Ao clicar novamente no elemento, a sua classe deverá voltar a ser somente task, ou seja, essa tarefa está deixando de ser uma tarefa selecionada.
function addEventSelecionaTask () {
    function selecionaTask (event) {
        let classNeme = event.target.className 
        if (classNeme === "task" ) {
            event.target.classList.add('selected')
            console.log(event.target.className )
        } else {
            event.target.classList.remove('selected')
            console.log(event.target.className )
        }

    }
    const taskDiv = document.querySelectorAll(".task")
    for (elemeto of taskDiv) {
        elemeto.addEventListener('click' , selecionaTask)
    }
    
}
addEventSelecionaTask();

// 🚀 Exercício 10:
// Implemente uma função que atribua a cor da tarefa ao dia do calendário.
// Adicione um evento que, ao clicar em um dia do mês no calendário, atribua a esse dia a cor da legenda da sua tarefa selecionada.
// Ao clicar novamente no dia com a cor da legenda, a sua cor deverá voltar à configuração inicial rgb(119,119,119)






