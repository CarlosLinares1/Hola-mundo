#Ejercicio 1
n = str(input(" Ingrese un calificativo "))
print(" Carlos",n,)

#Ejercicio 2
y = 5
cuadrado = y ** y
print(cuadrado)

#Ejercicio 3
x = 4
m = 9
suma = x + m
print(m)

#Ejercicio 4 
p = 12
i = 15
sumaa = p + i
print(sumaa)
resta = p - i
print(resta)
multi = p * i
print(multi)
divi = p / i
print(divi)
resi = p % i
print(resi)

#Ejercicio 37
L = int(input("Ingrese un numero "))
K = int(input("Ingrese un numero "))
J = int(input("Ingrese un numero "))
if K > L:
    if J > K:
        print("Aumentando")
if K < L:
    if J < K:
        print("Disminuyendo")
if K == L:
    if J == L:
        print("Igual")

#Ejercicio 38
g = int(input("Ingrese un numero "))
f = int(input("Ingrese un numero "))
if (g >= 0 and g <= 5) and (f >= 0 and f <= 5):
    print("True")
else:
    print("False")