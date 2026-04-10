# Realiz un programa que calcule la media de un conjuto de elementos
# La media se realiza en una funcion que se le pasa el numero de elementos que lee y calcula la media 
# Exepcion --> que el usuario pase un numero 
 
'''Declaracion de funciones'''
def media(numero_elementos):
    c = 0
    for i in range(numero_elementos):
        x = int(input("Introduce el valor: "))
        c = c + x
    return c / numero_elementos

''' Programa principal'''    
num = int(input("introduce el numero de elementos: "))
print(f"La media es :{media(num)}")