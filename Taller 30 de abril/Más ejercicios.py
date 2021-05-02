#Ejercicio 7 - Programa que imprima el area y el perimetro de un circulo
radio = float(input("Ingrese el radio del cirulo: "))
pi = 3.14
areac = pi * (radio ** 2)
perimetro = (2 * pi) * radio
print("El area del circulo es: ", areac)
print("El perimetro del circulo es: ", perimetro)

#Ejercicio 6 - Programa que muestre la venta de un producto con y sin IVA
pan = 2000
IVA = (pan*19/100)
paniva = (pan+IVA)
print("El costo original del pan es: ", + pan, ",el IVA es de: ", + IVA, "Y el costo del pan con IVA es de: ", +paniva)

#Ejercicio 27 - Programa que pida dos numeros y determine el mayor
s = int(input("Ingrese un numero: "))
y = int(input("Ingrese un numero: "))
if s>y:
    print(s, "Es mayor que ", + y)
else:
    print(y, "Es mayor que ", + s)

#Ejercicio 28 - Programa que convierta un numero a decimal
p = int(input("Ingrese un numero: "))
deci = float(p)
print("El decimal del numero es = ", + deci)

#Ejercicio 29 - Programa que pida tres numeros y determine el mayor y el menor
t = int(input("Ingrese un numero: "))
x = int(input("Ingrese un numero: "))
z = int(input("Ingrese un numero: "))
if (t>x) and (t>z) and (x>z):
    print("El numero mayor es: ", + t, "Y el numero menor es: ", z)
else:
    if (t>x) and (t>z) and (z>x):
        print("El numero mayor es: ", + t, "Y el numero menor es: ", x)
    else:
        if (z>t) and (z>x) and (t>x):
            print("El numero mayor es: ", + z, "Y el numero menor es: ", x)
        else:
            if (z>t) and (z>x) and (x>t):
                print("El numero mayor es: ", + z, "Y el numero menor es: ", t)
            else:
                if (x>t) and (x>z) and (z>t):
                    print("El numero mayor es: ", + x, "Y el numero menor es: ", t)
                else:
                    if (x>t) and (x>z) and (t>z):
                        print("El numero mayor es: ", + x, "Y el numero menor es: ", z)
                    else:
                        print("Ingrese numeros diferentes")
