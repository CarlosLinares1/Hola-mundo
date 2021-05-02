#Ejercicios 30 - Programa que lee 3 numero y determina si la suma de los dos primeros es mayor que el tercero
g = int(input("Ingrese un numero: "))
h = int(input("Ingrese un numero: "))
l = int(input("Ingrese un numero: "))
suma = g+h
if suma > l:
    print("La suma de los dos primeros es mayor que el tercero ")
else:
    print("El tercero es mayor que la suma de los dos primeros")
print("Ya no hay más")

#Ejercicio 34 - Programa de inicio de sesión
def user_contraseña():
    user = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    clave = "willymidios123"
    usario = "vegetta777"
    if usario == user:
        if clave == contraseña:
            print("Inicio de sesión exitoso, turbo jhonathan")
    else:
        print("Mal, ingreselo bien")

user_contraseña()

#Ejercicio 5
num = float(input("Ingresa un numero decimal: "))
entera = int(num // 1)
decimal = num - entera
print("La parte entera es: ", entera, "y la parte decimal es: ", decimal)

#Ejercicio 8
import math
lado = float(input("Ingrese el valor de los lados del hexagono: "))
perimetro = lado * 6
apotema = math.sqrt(lado ** 2 - (lado / 2) ** 2)
area = (perimetro * apotema) / 2
print("El area del hexagono es: ", area)

#Ejercicio 9
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercero numero: "))
promedio = (n1+n2+n3) /3
print("El promedio es: ", promedio)