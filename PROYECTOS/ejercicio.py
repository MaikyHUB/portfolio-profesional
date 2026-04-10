opcion=0
while opcion != 3:
    print("1 notas")
    print("2 contar")
    print("3 salir")
    opcion = int(input("Elige la opcion: "))

    if opcion == 1:
        def notas():
            nombre = (input("Escriba tu nombre: "))
            modulo = (input("Escribe tu modulo:"))
            nota = int(input("Escriba tu nota: "))
            if nota < 0 or nota > 10:
                print("nota no valida")
            elif nota <= 4:
               print(f"el estudiante {nombre}ha sacado insuficiente en el modulo de {modulo}")
            elif nota <= 5:
                print(f"el estudiante {nombre}ha sacado suficiente en el modulo de {modulo}")
            elif nota <= 6:
                print(f"el estudiante {nombre}ha sacado bien en el modulo de {modulo}")
            elif nota <= 8:
                print(f"el estudiante {nombre}ha sacado notable en el modulo de {modulo}")
            else:
                print(f"el estudiante {nombre}ha sacado sobresaliente en el modulo de {modulo}")
        notas()
    elif opcion == 2:
        def contar():
            ini = int(input("Escribe el inicio de la cuenta: "))
            fin = int(input("Escribe el fin de la cuenta: "))
            salto = int(input("Escribe el salto de la cuenta: "))
            for i in range(ini,fin,salto):
                print(i)
        contar()
             
    else:
        print("ERROR")