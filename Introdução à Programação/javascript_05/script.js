let quantidadeSubtotal = document.getElementById("quantidade-subtotal");
let valorSubtotal = document.getElementById("valor-subtotal");

let subtotalInfo = {
  quantidade: 1,
  valor: 11.66,
};

quantidadeSubtotal.innerText = subtotalInfo.quantidade + " itens";
valorSubtotal.innerText = subtotalInfo.valor;


const inputQtdMais = document.getElementById('quantidade-produto-01')
const btnQtdMais = document.getElementById('btn-adicionar-produto-01')

function adicionarQuantidadeMais() {
  inputQtdMais.value = Number(inputQtdMais.value) + 1
}

btnQtdMais.addEventListener('click', adicionarQuantidadeMais)

const inputQtdMenos = document.getElementById('quantidade-produto-01')
const btnQtdMenos = document.getElementById('btn-subtrair-produto-01')

function adicionarQuantidadeMenos() {
    if (inputQtdMenos.value == 0) {
        return inputQtdMenos.value = 0
    } else {
        inputQtdMenos.value = Number(inputQtdMenos.value) - 1
    }
  }

btnQtdMenos.addEventListener('click', adicionarQuantidadeMenos)

 
