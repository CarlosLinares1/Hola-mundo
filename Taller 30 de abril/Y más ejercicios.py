#Ejercicio 11
import math
h = int(input("Ingrese la altura: "))
g =  10
tiempo = math.sqrt(2*h/g) #Formula de tiempo
print("El tiempo en segundos es: ", tiempo)

#Ejercicio 14
m = float(input("Ingrese la masa del objeto"))
vl = 299792458 #Velocidad de la luz
e = m * (vl ** 2) #Formula de energía

print("La energia del objeto es: ", e)
#Ejercicio 16
s = int(input("Ingrese los segundos: "))
h = (s * 1/3600) #Formula de segundos a horas
print("Los segundos en horas son: ", h)

#Ejercicio 17
s = int(input("Ingrese los segundos: "))
m = (s * 1/60) #Formula de segundos a minutos
print("Los segundos en minutos son: ", m)

#Ejercicio 18
Horadia = int(input("Ingrese los segundos: "))
Hora = Horadia * 1/3600
Minutos = Horadia * 1/60 
Segundos = Horadia
print(Hora,":",Minutos,":",Segundos)

#Ejercicio 19
dinero = int(input("Ingrese la cantidad de dinero: "))
mil = dinero/1000
dosmil = dinero/2000
cinco = dinero/5000
diez = dinero/10000
veinte = dinero/20000
cinco = dinero/50000
print("La cantidad de billetes de mil ", mil, ",de dosmil", dosmil, ",de cincomil ", cinco, ", de diezmil", diez, ", de vientemil", veinte, "y de cincuentamil", cinco)

