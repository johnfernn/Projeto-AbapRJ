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
    card.classList.toggle('active')

    if (card.classList.contains('active')){
        return button.textContent = 'Leia menos'
    }
    return button.textContent = 'Leia mais'
})