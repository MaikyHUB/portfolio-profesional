# def factorial(n):
#     f = 1
#     for i in range (1,n+1):
#         f = f*i
#     return f
# x = int(input("Introduce el numero: "))
# print(f"El resultado es: {factorial(x)}")


# Ejercicio 1: El contador de ovejas insomnes
# Enunciado:#
# Un pastor quiere contar ovejas para dormirse, pero el programa no funciona correctamente.
# La función debería devolver el número total de ovejas contadas.
# def contar_ovejas(ovejas):
#     total = 0
#     for i in range(ovejas):
#         total = total + i
#     return total
# print(contar_ovejas(10))


# Ejercicio 2: La pizzería caótica
# Enunciado:
# Una pizzería quiere calcular el precio final de un pedido.
# Cada pizza cuesta 8 €, y si el cliente pide más de 3 pizzas tiene un descuento del 10%.
# def precio_pedido(numero_pizzas):
#     precio = numero_pizzas * 8
#     if numero_pizzas > 3:
#         precio = precio - (precio * 0.1)
#     return precio

# print(precio_pedido(5)) 

# Ejercicio 3: El mago y el hechizo fallido
# Enunciado:
# Un mago lanza un hechizo que debería duplicar su poder mágico, pero algo sale mal.
# def lanzar_hechizo(poder):
#     poder = poder * 2
#     return poder
# resultado = lanzar_hechizo(7)
# print(f"El poder del hechizo es: {resultado}")

# Ejercicio 9: El tesoro pirata mal contado
# Enunciado:
# Un pirata reparte monedas de oro entre su tripulación.
# La función debería devolver cuántas monedas recibe cada pirata y cuántas sobran.
# def repartir_tesoro(moneda_totales, piratas):
#     monedas_por_pirata = moneda_totales // piratas
#     sobrantes = moneda_totales % piratas
#     return monedas_por_pirata, sobrantes

# print(repartir_tesoro(100, 6))