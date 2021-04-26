#Ejercicio 5
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #Se almacena una lista con las letras del abecedario
for i in range(len(alfabeto), 1, -1):
    if i % 3 == 0: #Las letras que esten en la 3ra posición no se mostraran
        alfabeto.pop(i-1)    #Con la función .pop se elimina los números multiplos de 3
print(alfabeto)
#Ejercicio 6
palabras = ["sometemos" , "arenera" , "ana" ,"oso"]
for palabra in palabras:
    if(palabra==palabra[::-1]):
        print("Es palindromo")
    else:
        print("Paila")
#Ejercicio 7
P = int(input("Ingrese cuantos pedidos: "))
B = []
C = []
for j in range (0,P):
    B.append(input("Ingrese su pedido: "))
print("Su comida: ", B)
for z in range(0,P):
    C.append(len(B[(z)]))
print("La cantidad de letras de su comida es: ", C)
