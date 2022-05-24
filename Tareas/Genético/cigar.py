def calc_FO(indv):
    suma=0.0
    for i in range(1,len(indv)):
        suma+=indv[i]**2
    return indv[0]+pow(10,6)*suma

tot_genes = 10
tot_individuos = 100
probMuta = 0.85
tot_padres = 50

import random as rnd
poblacion = []
for i in range(tot_individuos):
    vector = [ rnd.uniform(-10,10)  for i in range(tot_genes)]
    poblacion.append([vector, calc_FO(vector)])

it = 1
mejorActual = pow(10,15)
while it<=200:
    it+=1
    padres = []

    poblacion.sort(key= lambda x:x[1], reverse=False)

    if poblacion[0][1] <= mejorActual:
        mejorActual = poblacion[0][1]

    poblacion = poblacion[0:tot_individuos-tot_padres]

    for i in range(tot_padres):
        indexPadre1 = rnd.randint(0, tot_padres-1) #aleatorio entre 0 y n-1
        indexPadre2 = rnd.randint(0, tot_padres-1) #aleatorio entre 0 y n-1
        while(indexPadre1==indexPadre2):
            indexPadre2 = rnd.randint(0, tot_padres - 1)  # aleatorio entre 0 y n-1

        tempPadre1 = poblacion[indexPadre1]
        tempPadre2 = poblacion[indexPadre2]

        if tempPadre1[1] <= tempPadre2[1]:
            padres.append(tempPadre1[0].copy())
        else:
            padres.append(tempPadre2[0].copy())

    hijos = []
    for i in range(0,tot_padres, 2):
        tempPadre1 = padres[i]
        tempPadre2 = padres[i+1]

        puntoCruza = rnd.randint(0, tot_genes-1)

        puntoCruza += 1
        hijo1 = tempPadre1[:puntoCruza] + tempPadre2[puntoCruza:]
        hijo2 = tempPadre2[:puntoCruza] + tempPadre1[puntoCruza:]

        hijos.append([hijo1, 0])
        hijos.append([hijo2, 0])

    for indexHijo in range(len(hijos)):
        hijo = hijos[indexHijo][0]
        for indexGen in range(len(hijo)):
            r = rnd.random() # 0 - 1
            if r >= probMuta:
                if(rnd.random()>=0.5):
                    val = rnd.uniform(0,0.5)
                else:
                    val=rnd.uniform(0.51,1)

                hijo[indexGen] = hijo[indexGen]*val

        hijos[indexHijo][1] = calc_FO(hijo)

    poblacion += hijos

print("Mejor Solucion Actual:" , mejorActual)