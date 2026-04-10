#Esta linea de codigo imprime por pantalla esta linea de codigo
'''Este es un comentario de varias lineas. Las tres comillas son para el multilienas '''
print("hola mundo")

#una variable son elemenos que contienen datos 

#--------------------------------------------------------------#


#tipos de datos
Primitivos e inmutables: int (enteros), float (flotantes), str (cadenas de texto), complex (números complejos) y bool (booleanos). 
Colecciones inmutables: tuple (tuplas) y frozenset (conjuntos inmutables). 
Colecciones mutables: list (listas), dict (diccionarios) y set (conjuntos). 
Otros tipos: NoneType (ausencia de valor), range (rangos), bytes, bytearray y memoryview


# Definición de variables
a = 10
b = 3

# Suma
suma = a + b
print(f"Suma: {a} + {b} = {suma}")

# Resta
resta = a - b
print(f"Resta: {a} - {b} = {resta}")

# Producto
producto = a * b
print(f"Producto: {a} * {b} = {producto}")

# División (float) devuelve el cociente como número decimal.
division = a / b
print(f"División (float): {a} / {b} = {division}")

# División Entera (floor division) devuelve solo la parte entera del cociente.
division_entera = a // b
print(f"División Entera: {a} // {b} = {division_entera}")

# Módulo (residuo) devuelve lo que sobra después de dividir.
modulo = a % b
print(f"Módulo: {a} % {b} = {modulo}")

# Exponente (potencia)
exponente = a ** b
print(f"Exponente: {a} ** {b} = {exponente}")

#--------------------------------------------------------------#


# Definimos dos valores booleanos

#Operadores logicos (and)
x = int(input("Introduce un valor:"))  
z = (x > 1) and (x > 5)  # Compara si x es mayor que 1 y si x también es mayor que 5
print(f"El resultado es {z}") 


#Operadores logicos (or)
x = int(input("Introduce un valor: "))  
z = (x == 5) or (x == 8)  # Evalúa si x es igual a 5 o si x es igual a 8
print(f"El resultado es {z}")  


#Operadores logicos (not)
x = int(input("Introduce un valor:"))  
z = (x == 5)  # Compara si el valor de x es igual a 5. Devuelve True si es cierto, False si no lo es.
print(f"El resultado es {z}")



#--------------------------------------------------------------#
if condición:
    # Código que se ejecuta si la condición es verdadera
else:
    # Código que se ejecuta si la condición es falsa

