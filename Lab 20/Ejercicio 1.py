#Programa principal - Se mejoro la interración con el usuario y se movio "numero"
def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

 
def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

 
def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f

 
def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma

 
mayor=0
numero=int(input("Ingrese un numero primo "))
while primo(numero):
    print("La suma de los digitos es: ",sumaDigitos(numero))
    digito=int(input("Dígito: "))
    print("El",digito,"aparece",frecuencia(numero,digito),"veces")
    numero=int(input("Ingrese otro numero primo "))
    if numero > mayor:
        mayor=numero
print("El factorial de",mayor,"es :",factorial(mayor))
print("Gracias")
