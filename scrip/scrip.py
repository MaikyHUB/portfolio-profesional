# navegar entre carpetas
import os

def navegar():
    print(os.getcwd()) #printea donde estamos 
    os.chdir("C:/Users/2smr/Desktop/portfolio/subcarpeta/maiky") #te mueve a una carpeta
    print(os.getcwd()) #printea donde estamos 
    os.chdir("C:/Users/2smr/Desktop/portfolio/subcarpeta") #regresa 
    print(os.getcwd())

navegar()  

def listar():
    os.chdir("C:/Users/2smr/Desktop/portfolio/subcarpeta/maiky")
    data = os.listdir()
    for i in data:
        print(i)

listar()

def rename():
    os.chdir("C:/Users/2smr/Desktop/portfolio/subcarpeta/maiky")
    for file in os.listdir():
        name, ext = os.path.splitext(file)
        new_name = f"new-{name}{ext}"
        os.rename(file, new_name)