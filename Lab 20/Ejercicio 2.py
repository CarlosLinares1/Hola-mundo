#Programa principal - Se mejoro el print final y se le quito "coordenadaZ" en la z, y se quito codigo basura
x=int(input("Coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
  z=(x,y)
  x=x+1
  y=y+1
print("Coordenada x: ", x, " . " , "Coordenada y: ", y)
