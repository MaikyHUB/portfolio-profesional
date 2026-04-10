// js/validacion.js
// Script 1 – Validación del formulario de contacto

const form = document.getElementById('formularioContacto');
if (form) {
  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const nombre = document.getElementById('nombre');
    const email = document.getElementById('email');
    const mensaje = document.getElementById('mensaje');
    const exitoMsg = document.getElementById('exito-msg');

    let valido = true;

    // Limpiar errores anteriores
    limpiarError(nombre, 'error-nombre');
    limpiarError(email, 'error-email');
    limpiarError(mensaje, 'error-mensaje');
    exitoMsg.textContent = '';

    // Validar nombre
    if (nombre.value.trim() === '') {
      mostrarError(nombre, 'error-nombre', 'El nombre es obligatorio.');
      valido = false;
    }

    // Validar email
    if (email.value.trim() === '') {
      mostrarError(email, 'error-email', 'El correo es obligatorio.');
      valido = false;
    } else if (!validarEmail(email.value.trim())) {
      mostrarError(email, 'error-email', 'El correo no tiene un formato válido.');
      valido = false;
    }

    // Validar mensaje
    if (mensaje.value.trim() === '') {
      mostrarError(mensaje, 'error-mensaje', 'El mensaje no puede estar vacío.');
      valido = false;
    }

    // Si todo es correcto
    if (valido) {
      exitoMsg.textContent = '✅ Mensaje enviado correctamente. ¡Gracias!';
      form.reset();
    }
  });
}

function mostrarError(campo, idSpan, texto) {
  campo.classList.add('invalido');
  document.getElementById(idSpan).textContent = texto;
}

function limpiarError(campo, idSpan) {
  campo.classList.remove('invalido');
  document.getElementById(idSpan).textContent = '';
}

function validarEmail(email) {
  // Expresión regular para formato de email válido
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}
