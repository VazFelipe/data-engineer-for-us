let h1 = document.getElementById('titulo');

let listaNaoOrdenada = document.getElementById('lista-naoordenada')
let mensagem = ["Very", "Nice", "OMG"];

let hrefAtributo = document.querySelector("[href='https://prozeducacao.com.br']");

let listaOrdenada = document.getElementById("lista-ordenada");
let links = ["https://www.google.com", "https://www.microsoft.com", "https://www.amazon.com.br"]

h1.innerText = "Hey, let's do this!"

for (i = 0; i < mensagem.length; ++i) {
    let li = document.createElement('li');
    li.innerHTML = mensagem[i];
    listaNaoOrdenada.appendChild(li);
}

hrefAtributo.innerText = 'Click to follow Proz Educação'

for (let i = 0; i < links.length; i++) {
    let li = document.createElement("li");
    listaOrdenada.appendChild(li);

    let link = document.createElement("a");
    link.setAttribute("target", "_blank")
    link.setAttribute("href", links[i]);
    link.innerHTML = links[i]
    li.appendChild(link);
}