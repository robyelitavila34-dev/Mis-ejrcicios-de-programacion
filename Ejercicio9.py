#Ejercicio9 : Calcular el promedio de varias notas 

#Variable para contar las notas 
n_notas= int(input("¿Cuantas notas va ingresar?: \n "))
#Variable contenida de letras 
letras = "abcdefghijklmñopqrstuvwxyzABCDEFGHIJKLMÑOPQRSTUVWXYZ"
#Variable para sumar las notas 
suma_notas = 0
#contador para contar las notas 
cont = 0
#Variable para almacenar las notas 
notas  = 0 
#Ciclo para infinito por no saber cuantas notas va ingresar
while  range(n_notas) :
     notas= float(input("Ingrese su nota: \n"))
     suma_notas =suma_notas + notas
     cont =+ 1  

     #Condicional por si el usuario coloca algo que no sea numero
     if notas == 0 :
          print("Este valor no es una nota , ingrese otro... ")

     elif notas == letras :
          print("Esta nota no es un numero es un caracter , vuelva a intentarlo...")
     else:
          print("Notas incorrectas vuelva a intertarlo...")
          break

#Variable calculaodra del promedio
promedio = suma_notas / n_notas

#Mostrando a la pantalla 
print("===Resultado===")
print(f"Tu promedio de notas es : {promedio}")



