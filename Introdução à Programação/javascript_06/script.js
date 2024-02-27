const linkPerfil = document.getElementById("link-perfil");
const navPerfil = document.getElementById("nav-perfil");
const linkPerfilDados = document.getElementById("link-perfil-dados");

document.addEventListener('keyup', (e) => {
  console.log('key:', e.key)
  console.log('code:', e.code)

if(navPerfil.style.display == 'block') {

  if(e.code == 'Digit1') {
  linkPerfilDados.click()
  } }else {
    navPerfil.style.display = "block"
  }

  if(e.code == 'Escape') {
    navPerfil.style.display = "none"
  }  
})