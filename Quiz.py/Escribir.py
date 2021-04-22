dias = [ "0" , "Lunes" , "Martes" , "Miercoles" , "Jueves" , "Vienes" , "Festivo" ,"Festivo"]
numero = int(input("Ingrese numero del día que quieras "))
print("El día es" + " " + str(numero) + " Es = " + str(dias[numero ]))

def imprimir_tabla(numero):
    LIMITE = 10
    contador = 1
    while contador <= LIMITE:
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))  
        contador = contador + 1
imprimir_tabla(1)
