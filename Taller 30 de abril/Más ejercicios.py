#Ejercicio 7 - Programa que imprima el area y el perimetro de un circulo
r = 5
areac = 3,14 * r ** 2
perimetro = 2 * 3,14 * r
print("El area del circulo es: ", areac, "y el perimetro es: ", perimetro)
#Ejercicio 6 - Programa que muestre la venta de un producto con y sin IVA
pan = 2000
IVA = (pan*19/100)
paniva = (pan+IVA)
print("El costo original del pan es: ", + pan, ",el IVA es de: ", + IVA, "Y el costo del pan con IVA es de: ", +paniva)
#Ejercicio 27 - Programa que pida dos numeros y determine el mayor
s = int(input("Ingrese un numero: "))
z = int(input("Ingrese un numero: "))
if s>z:
    print(s, "Es mayor que ", + z)
else:
    print(z, "Es mayor que ", + s)

#Ejercicio 28 - Programa que convierta un numero a decimal
p = int(input("Ingrese un numero: "))
deci = float(p)
print("El decimal del numero es = ", + deci)

#Ejercicio 29 - Programa que pida tres numeros y determine el mayor y el menor
t = int(input("Ingrese un numero: "))
x = int(input("Ingrese un numero: "))
y = int(input("Ingrese un numero: "))
if t>x:
    if t>y:
        print("El numero mayor es: ", + t)
elif x>t and x>y:
    print("El numero mayor es: ", + z)
else:
    print("El numero mayor es ", + y)

if t<x:
    if t<y:
        print("El numero menor es: ", + t)
elif z<t and z<t:
    print("El numero menor es: ", + z)
else:
    print("El numero menor es: ", + y)
