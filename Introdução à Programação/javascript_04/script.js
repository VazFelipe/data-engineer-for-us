// const h2 = document.querySelector('h2')
// const label = document.querySelector('label')
// const button = document.querySelector('button')


// h2.style.color = 'red'
// h2.style.fontSize = '80px'
// label.style.color = 'yellow'
// label.style.fontSize = '30px'
// button.style.backgroundColor = 'green'

const userName = document.querySelector('#login-usuario')
const userPassword = document.querySelector('#login-senha')
const p1 = document.querySelectorAll('.error-text')[0]
const p2 = document.querySelectorAll('.error-text')[1]

// userName.classList.add('error')
// p1.classList.add('visible')
userPassword.classList.add('error')
p2.classList.add('visible')

function validateForm() {
    if (userName.value.length == 0) {
        userName.classList.add('error');
        p1.classList.add('visible');
    } else {
        userName.classList.remove('error');
        p1.classList.remove('visible');
    }
  }

validateForm()