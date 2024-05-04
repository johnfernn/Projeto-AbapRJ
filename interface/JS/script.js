// Carrosel
let contador = 1;

setInterval( function(){
    document.getElementById('slide' + contador).checked = true;
    contador++;

    if(counter > 5 ) {
        contador = 1;
    }
}, 3000 );

//Sobre o projeto
var botao = document.getElementById('read_button')

botao.addEventListener('click', function(){
    var card = document.querySelector('.sobreOProjeto')
    var imagem = document.getElementById('iconeSeta')
    var texto = document.getElementById('descritivo')
    card.classList.toggle('active')

    if(imagem.src.includes('imagens/SetaParaBaixo.svg')){
        imagem.src = 'imagens/SetaParaCima.svg'
        imagem.alt = 'Seta para cima'
    } else {
        imagem.src = 'imagens/SetaParaBaixo.svg'
        imagem.alt = 'Seta para baixo'
    }

    if(texto.textContent == 'Leia mais'){
        texto.textContent = 'Leia menos'
    } else {
        texto.textContent = 'Leia mais'
    }
})

