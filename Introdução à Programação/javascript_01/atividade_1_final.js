const senha = 'minhasenha'
const email = 'jeff@gmail.com'
const permissao = true
const id = 1234

let senhaUsuario = 'minhasenha'
let emailUsuario = '_jeff@gmail.com'
let idUsuario = 1234
let permissaoUsuario = false

if(emailUsuario === email && idUsuario === id) {
    console.log('Deseja mudar a senha?')
} else {
    console.log('Usuario sem permissão !! ')
};

if(senha === senhaUsuario && email === emailUsuario) {
    console.log('Por favor, insira sua nova senha')
} else {
    console.log('Username / senha incorretos')
};

if(permissao === permissaoUsuario) {
    console.log('Bem-vindo(a) à área de administrador')
} else {
    console.log('Você não pode acessar esta parte do sistema')
};