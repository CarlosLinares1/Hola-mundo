#Ejercicio 1
for n in range (0,10):
    print(n)
#Ejercicio 2
print("Numeros entre el 100 y 199")
for n2 in range (101,200):
    print(n2)
#Ejercicio 3
print("Numeros entre 5 y 20, de tres en tres")
for n3 in range (5,21,3):
    print(n3)
#Ejercicio 4
x = int(input("Ingrese un valor"))
for n4 in range (x,x*2):
    print(n4)
#Ejercicio 5 y 6
frase = input("frase: ")
print("Las vocales en la frase son")
for a in ("aeiou"):
    if a in frase:
        print(a)
#Ejercicio 7
i = 0
sum = 0
for i in range (i, 101 ,1):
    sum += i
print("Sumatoria de los numeros del 0 - 100: ", sum)
#Ejercicio 8
a1 = int(input("Ingresar año "))
a2 = int(input("Ingresar otro año "))
print ("Años biciestos entre los años " + str(a1) + "-" + str(a2) + "son: ")
for y in range (a1, a2+1):
    if y % 4 == 0 and not n % 100 == 0 or n % 400 == 0:
        print(y)
print ("Años multiplos de 10 entre los años " + str(a1) + "-" + str(a2) + "son: " )
for m in range (a1 , a2+1):
    if m % 10 == 0:
        print(m)
#Ejercicio 9
e = int(input("Ingrese un numero entero positivo: "))
fact = 1
for o in range (1, e+1,):
    fact = fact * o
print ("El factorial del numero " + str(e) + " es: " , fact)
#Ejercicio 10
print("Los 10 primeros numeros de la sucesión de Finobacci son: ")
nant = 0
nnue = 1
fibonacci = 0
print(nant)
print(nnue)
for x in range(1, 9, 1):
    fibonacci = nant + nnue
    nant = fibonacci - nant
    nnue = fibonacci
    print(fibonacci)