// Documento Object Modelo
console.log('Olá Mundo, nós somos o MELHOR GRUPO!!!!!!')

// const lista_redes = document.getElementsByClassName('lista_redes');
// const post01 = document.getElementById('post01')
// const post02 = document.getElementById('post02')
// const formulario = document.getElementById('formulario')
// const section = document.getElementsByTagName('section')
// const post_data = document.getElementsByTagName('p')[1]
// const dataPosts = document.getElementsByClassName('post-data')
// const textoPosts = document.getElementsByClassName('post')
// const sectionId = document.getElementById('posts')
 
// console.log(lista_redes)
// console.log(post01)
// console.log(post02)
// console.log(formulario)
// console.log(section)
// console.log(post_data)
// console.log(dataPosts[1].innerText)
// console.log(sectionId.innerText)

// post02 //
// formulário
// section
// data dos posts
// textos dos posts



// const h1 = document.querySelector('h1')
// const elementos_nav = document.querySelector('.elementos_nav')
// const post01 = document.querySelector('#post01')
// const elementosNav = document.querySelectorAll('.elementos_nav')
// const h3 = document.querySelectorAll('h3')
// console.log(h3[2])

const linkPost = document.querySelector('.post-texto')
 
// - O link dentro do texto do primeiro post
console.log(linkPost.querySelector('a').innerText)
// - A palavra em negrito dentro do texto do segundo post
// - O input de nome do formulário
// - Os links da lista de redes no final da página
// - Os links da navegação (só os links, não os elementos de lista)
// - Os 4 "Autor:" e "Data:" em negrito nos dois posts'


let titulos = document.querySelectorAll('footer .lista_redes a')

function imprimirTodos(lista) {
for (let i = 0; i < titulos.length; i++) {
console.log(titulos[i]. innerHTML)
}
}

imprimirTodos(titulos)
