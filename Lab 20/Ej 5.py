#Programa principal - Se le dio la posilidad al usuario que ingrese un numero para hallar su factorial
def fun_fact(x):
 if (x==1):
   return 1
 else:
   x=(x*fun_fact(x-1))
 return x
num = int(input("Ingrese un numero"))
print ("El factorial de ", num, "es ", fun_fact(num)) 
print("Gracias")