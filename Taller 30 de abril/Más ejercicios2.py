#Ejercicio 29 - Programa que pida tres numeros y determine el mayor y el menor
t = int(input("Ingrese un numero: "))
x = int(input("Ingrese un numero: "))
y = int(input("Ingrese un numero: "))
if (t > x)  and (t > y) and (x < y):
    print("El numero mayor es: ", + t, "Y el numero menor es: ", + y)
else:
    if (x > t) and (x > y) and (t < y):
        print("El numero mayor es: ", + x, "Y el menor es: ", + y)
    else:
        if (y > t) and (y > x) and (x < t):
            print("El numero mayor es: ", + y, "Y el menor es: ", + t)
print("Se acabo, crack")

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
        print("Bobo hpta")

user_contraseña()