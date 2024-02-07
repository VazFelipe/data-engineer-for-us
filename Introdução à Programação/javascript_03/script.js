const arrayPostagens = [
  {
    titulo: "Pop Vegan",
    subtitulo: "Comida vegana para todos!",
    data: "06/07/2022",
    texto: "Restaurante em Consolação com comida por kilo no almoço e rodízio de pizzas à noite, tudo 100% vegano. Vale muito a pena conhecer :)"
  },
  {
    titulo: "Make Hommus. Not War",
    subtitulo: "Só delivery, para curtir em casa!",
    data: "18/08/2022",
    texto: "Neste restaurante não só pode, como é encorajado comer o antepasto como prato principal. Recomendamos os kibes e a kafta bonina."
  },
  {
    titulo: "Churrascada do Mar",
    subtitulo: "Melhor do que estar na praia!",
    data: "30/08/2022",
    texto: "Todos conhecemos e amamos um bom churrasco, mas o que você acha de experimentar um churrasco focado em frutos do mar? Nós gostamos, experimente e nos conte o que você achou!"
  },
]

// Criando elemento
// const article_0 = document.createElement('article')
// const article_1 = document.createElement('article')
// const article_2 = document.createElement('article')


// Populando o elemento

for(let i = 0; i < arrayPostagens.length; i++){
  const article = document.createElement('article')
  
  article.innerHTML = `
  <h3>${arrayPostagens[i].titulo}</h3>
  <p class="subtitulo">${arrayPostagens[i].subtitulo}</p>
  <div class="data">${arrayPostagens[i].data}</div>
  <p>${arrayPostagens[i].texto}</p>`  

  const main = document.querySelector('main')
  main.appendChild(article)
} 

// article_0.innerHTML = `
// <h3>${arrayPostagens[0].titulo}</h3>
// <p class="subtitulo">${arrayPostagens[0].subtitulo}</p>
// <div class="data">${arrayPostagens[0].data}</div>
// <p>${arrayPostagens[0].texto}</p>`

// article_1.innerHTML = `
// <h3>${arrayPostagens[1].titulo}</h3>
// <p class="subtitulo">${arrayPostagens[1].subtitulo}</p>
// <div class="data">${arrayPostagens[1].data}</div>
// <p>${arrayPostagens[1].texto}</p>`

// article_2.innerHTML = `
// <h3>${arrayPostagens[2].titulo}</h3>
// <p class="subtitulo">${arrayPostagens[2].subtitulo}</p>
// <div class="data">${arrayPostagens[2].data}</div>
// <p>${arrayPostagens[2].texto}</p>`

// Adicionando no DOM
// const main = document.querySelector('main')
// main.appendChild(article_0)
// main.appendChild(article_1)
// main.appendChild(article_2)