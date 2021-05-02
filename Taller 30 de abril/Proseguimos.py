#Ejercicio 44
n = int(input("Ingrese un numero: "))
for i in range(1, n + 1,1):
    print(i)

#Ejercicio 48
sum = 0

for i in range(1, 11, 1):
    N = int(input("Ingresa un numero para sumar: "))
    sum = sum + N

prom = Suma / 10
print("La suma de los numeros es de: ", sum)
print("El promedio es de: ", prom)

#Ejercicio 51
p = -1

while p < 0:
    p = int(input("Ingresa un numero entero positivo: "))
    if p > 0:
        print("El numero", p, "es entero positivo")
    elif p < 0:
        print("El numero ingresado no es valido, ingrese otro")