def maximo(x,y):
  if x>y:
    return x
  else:
    return y

 
def minimo(x,y):
  if x<y:
    return x
  else:
    return y

 
#Programa principal - La profe puso a y b en vez de x y y jajaja
x=int(input("Ingrese un numero: "))
y=int(input("Ingrese otro numero: "))
print(maximo(x-3, minimo(x+2, y-5)))
