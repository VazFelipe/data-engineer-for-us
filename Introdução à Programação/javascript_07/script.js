// ---------- VALIDAÇÃO USERNAME ---------- //
let usernameInput = document.getElementById("username");
let usernameLabel = document.querySelector('label[for="username"]');
let usernameHelper = document.getElementById("username-helper");

let emailInput = document.getElementById("email");
let emailLabel = document.querySelector('label[for="email"]');
let emailHelper = document.getElementById("email-helper");

let idadeInput = document.getElementById("idade");
let idadeLabel = document.querySelector('label[for="idade"]');
let idadeHelper = document.getElementById("idade-helper");


// Mostrar popup de campo obrigatório
usernameInput.addEventListener('focus', function(){
    usernameLabel.classList.add('required-popup')
})

emailInput.addEventListener('focus', function(){
    emailLabel.classList.add('required-popup')
})

// Ocultar popup de campo obrigatório
usernameInput.addEventListener('blur', function(){
    usernameLabel.classList.remove('required-popup')
})

emailInput.addEventListener('blur', function(){
    emailLabel.classList.remove('required-popup')
})

// Validar valor do input
usernameInput.addEventListener('change', function(evento){
    let valor = evento.target.value
    if (valor.length < 4){
        usernameInput.classList.add('error')
        usernameHelper.classList.add('visible')
        usernameInput.classList.remove('correct')
    } else {
        usernameInput.classList.remove('error')
        usernameHelper.classList.remove('visible')
        usernameInput.classList.add('correct')
    }
})

// Validar valor do email
emailInput.addEventListener('change', function(evento){
    let valor = evento.target.value
    if (valor.includes("@") && valor.includes(".com") ){
        emailInput.classList.remove('error')
        emailHelper.classList.remove('visible')
        emailInput.classList.add('correct')
    } else {
        emailInput.classList.add('error')
        emailHelper.classList.add('visible')
        emailInput.classList.remove('correct')
    }
})

// ALTERNATIVA PARA MOSTRAR REQUIRED POPUP E N PRECISAR REESCREVER CÓDIGO
function mostrarPopup(input, label){
    // Mostrar popup de campo obrigatório
    input.addEventListener('focus', function(){
        label. classList.add('required-popup')
    })
    // Ocultar popup de campo obrigatório
    input.addEventListener('blur', function(){
        label.classList.remove('required-popup')
    })
}

// Validar valor da idade
mostrarPopup(idadeInput, idadeLabel)

idadeInput.addEventListener('change', function(evento){
    let valor = evento.target.value
    if (valor < 18 ){
        idadeInput.classList.add('error')
        idadeHelper.classList.add('visible')
        idadeInput.classList.remove('correct')
    } else {
        idadeInput.classList.remove('error')
        idadeHelper.classList.remove('visible')
        idadeInput.classList.add('correct')
    }
})
