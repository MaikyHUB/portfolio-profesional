javascript// Cargar carrito guardado (si existe)
let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

// Agregar producto
function agregarAlCarrito(nombre, precio) {
    let producto = carrito.find(p => p.nombre === nombre);
    
    if (producto) {
        producto.cantidad++;  // Si ya existe, aumenta cantidad
    } else {
        carrito.push({ nombre, precio, cantidad: 1 });
    }
    
    guardarCarrito();
    alert(`✅ ${nombre} agregado al carrito`);
}

// Guardar en localStorage
function guardarCarrito() {
    localStorage.setItem('carrito', JSON.stringify(carrito));
    mostrarCarrito();
}

// Mostrar productos en pantalla
function mostrarCarrito() {
    let contenedor = document.getElementById('carrito');
    let total = 0;
    
    if (carrito.length === 0) {
        contenedor.innerHTML = '<p>El carrito está vacío</p>';
    } else {
        contenedor.innerHTML = carrito.map(p => `
            <div>
                <span>${p.nombre}</span>
                <span>x${p.cantidad}</span>
                <span>$${(p.precio * p.cantidad).toFixed(2)}</span>
                <button onclick="eliminarProducto('${p.nombre}')">❌</button>
            </div>
        `).join('');
        
        total = carrito.reduce((sum, p) => sum + p.precio * p.cantidad, 0);
    }
    
    document.getElementById('precio-total').textContent = total.toFixed(2);
}

// Eliminar un producto
function eliminarProducto(nombre) {
    carrito = carrito.filter(p => p.nombre !== nombre);
    guardarCarrito();
}

// Vaciar todo
function vaciarCarrito() {
    carrito = [];
    guardarCarrito();
}

// Mostrar al cargar la página
mostrarCarrito();