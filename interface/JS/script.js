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
var button = document.getElementById('read_button')

function ajustaCaixa(){
    var caixa = this.querySelector('#sobreOProjeto')
}

button.addEventListener('click', function(){
    var card = this.querySelector('#sobreOProjeto')
    card.classList.toggle('active')

    if (card.classList.contains('active')){
        return button.textContent = 'Leia menos'
    }
    return button.textContent = 'Leia mais'
})