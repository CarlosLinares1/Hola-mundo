numero = int(input("Ingrese un numero "))
if numero % 5 == 0 and numero % 3 == 0:
    print("El numero si cumple")
else:
    print("El numero no cumple")
#Ejercicio 2
nota1 = int(input("Ingrese un numero "))
nota2 = int(input("Ingrese un numero "))
nota3 = int(input("Ingrese un numero "))
promedio = (nota1+nota2+nota3) / 3
if promedio >= 7:
    print("Promocionado")
elif promedio >= 4 and promedio<7:
    print("Regular")
else:
    print("Reprobado")
