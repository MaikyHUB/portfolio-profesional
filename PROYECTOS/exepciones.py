def dividir(x1,x2):
    try:
        resultado = x1/x2
    except (ZeroDivisionError,TypeError):
        print("No se puede dividir por cero y deben ser numeros")
    else:
        return resultado
    finally:
        print("Esto lo ejecuto yo por que yo lo valgo")
# print(f"{dividir (12,0)}")
# print(f"{dividir(12,"a")}")
# print(f"{dividir(12,2)}")