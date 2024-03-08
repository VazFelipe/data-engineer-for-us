let h1 = document.createElement('h1');
let section = document.createElement('section');
let h3 = document.createElement('h3');
let p = document.createElement('p');
let img = document.createElement('img');

h1.id = 'titulo'
h1.textContent = 'Loja gaudéria'
document.body.appendChild(h1)

section.id = 'produto'
document.body.appendChild(section)

h3.textContent = 'Erva mate'
section.appendChild(h3)

p.textContent = 'A erva-mate, também chamada mate ou congonha, é uma árvore da família das aquifoliáceas, originária da região subtropical da América do Sul. É consumida como chá mate, chimarrão ou tereré no Brasil, no Paraguai, na Argentina, no Uruguai, na Bolívia e no Chile.'
section.appendChild(p)

img.src = './img/erva_mate.png'
img.width = '400'
section.appendChild(img)

console.log(h1)
console.log(section)

