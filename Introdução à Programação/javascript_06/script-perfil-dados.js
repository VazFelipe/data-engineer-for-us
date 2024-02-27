const linkPerfilDados_v1 = document.getElementById("hyperlink-retornar-index");
const linkPerfilDados_v2 = document.querySelectorAll('perfil-main');

document.addEventListener('keyup', (e) => {
    console.log('key:', e.key)
    console.log('code:', e.code)
  
  if(e.code == 'Escape') {
    linkPerfilDados_v1.click()
  }
  })