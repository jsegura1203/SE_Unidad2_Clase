import numpy as np

archivo = open("matriz.csv","r")
contenido = archivo.readlines()
lista = [linea.split(",") for linea in contenido]
T = [ list(map(float,x))  for x in lista ]

for i in T:
    print(i)

E= [0.25,0.15,0.35,0.15,0.10]

Resultado1=E
n=int(input("\nIngrese el numero de estado que desea encontrar: "))
print("\nMétodo 1:")
for i in range (n):
    Resultado1 = np.dot(Resultado1,T)
    print ("Resultado1 :",str(i+1)," ",Resultado1)

print("\nMétodo 2:")

Resultado2=np.linalg.matrix_power(T, n)
Resultado2 = np.dot(E,Resultado2)
print("Resultado2:  ",n," ",Resultado2)




