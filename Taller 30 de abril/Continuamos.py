#Ejercicio 25
num = int(input("Ingrese un numero: "))
if num >= 10:
    tri = num * 3
    print("El triple del numero es", num)
else:
    cua = num / 4
    print("La cuarta parte del numero es", cua)
#Ejercicio 26
n1 = float(input("Ingrese la primera nota de 0-5 "))
n2 = float(input("Ingrese la segunda nota de 0-5 "))
n3 = float(input("Ingrese la tercera nota de 0-5 "))
n4 = float(input("Ingrese la cuarta nota de 0-5 "))
n5 = float(input("Ingrese la quinta nota de 0-5 "))
p1 = 0.15
p2 = 0.2
p3 = 0.15
p4 = 0.3
p5 = 0.2
prome = (n1 * p1 + n2 * p2 + n3 * p3 + n4 * p4 + n5 * p5)

if prome < 2:
    print("Paila mijo")
    print("Su promedio fue:", prome)
elif prome < 3:
    print("Perdio el año pa") 
    print("Su promedio fue: ", prome)
elif prome > 4.5:
    print("Su merced es un genio")
    print("Su promedio fue", prome)
elif prome >= 3:
    print("Afortunadamente paso")
    print("Su promedio fue", prome)

#Ejercicio 32
año = int(input("Ingresa un año:"))

if año % 4 == 0 or año % 400 == 0 or año % 100 == 0:
    print("El año es bisiesto")
else:
    print("El año no es Bisiesto")

#Ejercicio 35
nume = int(input("Ingrese un numero entre 0 y 10: "))
numeros = ["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]
print("El numero", nume, "es", numeros[nume])
#Ejercicio 36
l = int(input("Ingrese un numero: "))
can = len(str(l))
print("El numero ", l, "tiene", can, "digitos")