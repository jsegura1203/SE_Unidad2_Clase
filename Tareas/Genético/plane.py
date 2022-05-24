def calc_FO(indv):
    return indv[0]

tot_genes = 10

tot_individuos = 100

#Poblacion Inicial
import random as rnd
poblacion = []
for i in range(tot_individuos):
    vector = [ rnd.uniform(-10,10)  for i in range(tot_genes)]
    poblacion.append([vector, calc_FO(vector),abs(0-vector[0])])

it = 1
mejorActual = pow(10,15)
while it<=5:
    #print("Iteracion : ", it)
    it+=1
    padres = []
    tot_padres = 50
    poblacion.sort(key= lambda x:x[2], reverse=False)

    #for i in poblacion:
    #    print(i)

    if poblacion[0][2] <= mejorActual:
        mejorActual = poblacion[0][2]

    poblacion = poblacion[0:tot_individuos-tot_padres]

    ##Seleccion de los padres que seran cruzados
    for i in range(tot_padres):
        indexPadre1 = rnd.randint(0, tot_padres-1) #aleatorio entre 0 y n-1
        indexPadre2 = rnd.randint(0, tot_padres-1) #aleatorio entre 0 y n-1
        while(indexPadre1==indexPadre2):
            indexPadre2 = rnd.randint(0, tot_padres - 1)  # aleatorio entre 0 y n-1

        tempPadre1 = poblacion[indexPadre1]
        tempPadre2 = poblacion[indexPadre2]

        if tempPadre1[2] <= tempPadre2[2]:
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

        hijos.append([hijo1, 0, 0])
        hijos.append([hijo2, 0, 0])

    probMuta = 0.80

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
        hijos[indexHijo][2]=abs(0-hijos[indexHijo][1])

    poblacion += hijos

print("Mejor Solucion Actual:" , mejorActual)