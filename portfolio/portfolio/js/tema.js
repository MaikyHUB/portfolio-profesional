// js/tema.js
// Script 2 – Modo oscuro / modo claro

const btnTema = document.getElementById('toggleTema');

// Cargar preferencia guardada en localStorage
const temaGuardado = localStorage.getItem('tema');
if (temaGuardado === 'oscuro') {
  document.body.classList.add('oscuro');
  if (btnTema) btnTema.textContent = '☀️';
}

if (btnTema) {
  btnTema.addEventListener('click', function () {
    document.body.classList.toggle('oscuro');

    if (document.body.classList.contains('oscuro')) {
      btnTema.textContent = '☀️';
      localStorage.setItem('tema', 'oscuro');
    } else {
      btnTema.textContent = '🌙';
      localStorage.setItem('tema', 'claro');
    }
  });
}
