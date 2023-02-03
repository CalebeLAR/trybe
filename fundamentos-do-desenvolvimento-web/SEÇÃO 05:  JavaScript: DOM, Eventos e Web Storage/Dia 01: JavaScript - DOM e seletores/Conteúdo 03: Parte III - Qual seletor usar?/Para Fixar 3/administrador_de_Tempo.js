let cabeçalho = document.getElementById('header-container');
cabeçalho.style.backgroundColor = 'green';

let titulos_h3 = document.getElementsByTagName("h3");
for (let i = 0; i < titulos_h3.length; i++) {
    titulos_h3[i].style.color = "black" 
    // titulos_h3[i].innerText = "titulo: h" + i 
}
for (let i = 0; i < titulos_h3.length; i = i + 2) {
    titulos_h3[i].style.background = "green"
}

for (let i = 1; i < titulos_h3.length; i = i + 2) {
    titulos_h3[i].style.background = "blue"
}

// let primeiroBloquinho = document.getElementsByClassName("emergency-tasks");
// primeiroBloquinho[0].style.backgroundColor = "pink"

// let segundoBloquinho = document.getElementsByClassName("no-emergency-tasks");
// segundoBloquinho[0].style.backgroundColor = "pink"

let bloquinhos = document.getElementsByTagName("section");
bloquinhos[0].style.backgroundColor = "pink"
bloquinhos[1].style.backgroundColor = "yellow"

let rodapé = document.getElementById('footer-container');
rodapé.style.backgroundColor = 'green';





