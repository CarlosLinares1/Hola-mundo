#Ejercicio 1
n = int(input("Ingrese la cantidad de multiplos que quiere ver: ")) #Se le pide al usuario cuantos multiplos quiere ver del numero
m = int(input("Ingrese el numero del que quiere ver los multiplos: ")) #Este es el numero del que se veran los multiplos
a = [] #La lista donde se veran los multiplos
for i in range (1,n+1):
    a.append(i*m)
print (a) #Imprime a
#Ejercicio 2
A = int(input("Ingresa el numero de personas presentes: "))
B = [] #Lista de los nombres
C = [] #Lista de caracteres en el nombre
for i in range (0,A): #Se crea un for para los nombres
    B.append(input("Ingresa el nombre de las personas presentes: ")) #Se pregunta cuantas personas hay
print ("Nombre: ", B) #Se imprime el nombre de las peronas
for j in range (0,A): #Se crea un for para los caracteres
    C.append(len(B[j])) #Se crea un lectura de la cantidad de caracteres
print("Cantidad de letras en el nombre: ", C) #Se imprime la cantidad de caracteres en los nombres
#Ejercicio 3
materias = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje"] #Se crea la lista con las materias
resultados = [] #Se crea la lista de los resultados
for materia in materias: #Se crea un for para las materias
    resultado = input("¿Qué nota has sacado en " + materia + "?") #Pregunta la nota de la materia
    resultados.append(resultado)
for i in range(len(materias)):  #Se crea un for con las materias
    print("En " + materias[i] + " has sacado " + resultados[i]) #Y se pregunta las materias y los resultados
