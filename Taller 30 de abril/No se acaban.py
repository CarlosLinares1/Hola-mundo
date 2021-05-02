#Ejercicio 20
x = [1,2,3,4]
print(x)
x.reverse()
print(x)
#Ejercicio 21
num = int(input("Ingrese un numero: "))
if num%2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

#Ejercicio 22
s = int(input("Ingrese un numero: "))
if s>0:
    print("El numero es positivo")
elif s<0:
    print("El numero es negativo")
#Ejercicio 23
p = int(input("Ingrese un numero: "))
if p%2 == 0 and p>0:
    print("El numero es par y positivo")
elif p%2 != 0 and p<0:
    print("El numero es impar y negativo")
elif p%2 == 0 and p<0:
    print("El numero es par y negativo")
else:
    print("El numero es impar y positivo")
#Ejercicio 24
v = int(input("Ingrese el total de su compra: "))
IVA = v * 0.19
vyIVA = v + IVA
desc = v * 0.05
vtotal = vyIVA - desc
if v >= 150000:
    print("Su compra, con un valor de: ", v, "Más el IVA= ", vyIVA, "Con el descuento es= ", vtotal)
else:
    print("Su compra más el IVA es de: ", vyIVA)
