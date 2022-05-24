def Euclidiana(A, B):
    distancia = 0
    for i in range(len(A)):
        distancia += (A[i]-B[i])**2
    distancia = distancia ** (1/2)
    distancia = round(distancia, 2)
    return distancia

def Manhattan(A,B):
    distancia=0
    for i in range (len(A)):
        distancia+=abs(A[i]-B[i])
    return round(distancia,2)

def EuclidianaProm(A,B):
    distancia=0.0
    for i in range (len(A)):
        distancia += (A[i] - B[i])**2
    distancia=distancia/len(A)
    distancia=distancia**(1/2)
    return round(distancia,2)

def Canberra (A,B):
    distancia=0
    for i in range (len(A)):
        try:
            distancia+=abs(A[i]-B[i])/(abs((A[i]))+abs((B[i])))
        except:
            distancia+=0
    return round(distancia,2)

def Coseno(A,B):
    distancia=0
    arriba=0
    abajox=0
    abajoy=0
    for i in range(len(A)):
        arriba+=A[i]*B[i]
        abajox+=A[i]**2
        abajoy+=B[i]**2
    distancia=arriba/((abajox*abajoy)**(1/2))
    return round(distancia,2)

def Diferencia(A,B):
    distancia=0
    for i in range (len(A)):
        distancia += abs(A[i] - B[i])
    distancia=distancia/len(A)
    return round(distancia,2)

###CARGAR INSTANCIA DE ENTRENAMIENTO
#ARCHIVO DE ENTRENAMIENTO
archivo = open("wine_training90.0.csv","r")
contenido = archivo.readlines()

#VISUALIZA EL CONTENIDO DEL ARCHIVO
#print('\nArchivo Completo: ') #Impreso línea a línea
#for l in contenido:
#    print(l, end="") #por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
#print("\n\n")


lista = [linea.split(",") for linea in contenido]

#VISUALIZA LISTA PROCESADA
#print("Lista de listas separadas por comas: ")
#Impreso línea a línea
#for l in lista:
#    print(l)
#print("\n\n")


instancia = [ [ list(map(float,x[:13])), x[13] ] for x in lista ] #iris

print("Total de datos de la Instancia",len(instancia))

#print("Instancia de entrenamiento:")
#VISUALIZA EL CONTENIDO DEL ARCHIVO
#Impreso línea a línea
#for l in instancia:
#    print(l)
#print("\n\n")


##############################################################################
###CARGAR INSTANCIA DE PRUEBA
#ARCHIVO DE PRUEBA
archivo = open("wine_test90.0.csv","r")
contenido = archivo.readlines()

#VISUALIZA EL CONTENIDO DEL ARCHIVO
#print('\nArchivo Completo: ') #Impreso línea a línea
#for l in contenido:
#    print(l, end="") #por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
#print("\n\n")


lista = [linea.split(",") for linea in contenido]

#VISUALIZA LISTA PROCESADA
#print("Lista de listas separadas por comas: ")
#Impreso línea a línea
#for l in lista:
#    print(l)
#print("\n\n")

prueba = [ [ list(map(float,x[:13])), x[13] ] for x in lista ] #iris

print("Total de datos de la Instancia",len(prueba))

print("Instancia de prueba:")
#VISUALIZA EL CONTENIDO DEL ARCHIVO
#Impreso línea a línea
for l in prueba:
    print(l)
print("\n\n")

##############################################################################
###DEFINIR EL VALOR DE "K"  - Un número entre 1 y el total de registros de la instancia (entrenamiento)
Kmejor = 0
rendimiento=0
aciertos=0
##############################################################################
tamaño=round(len(instancia)/2,0)
for k in range(1, int(tamaño)):
    contAciertos = 0 #contador de aciertos obtenidos en la clasificación

    for registroNC in prueba: #para recorrer a todos los registros de prueba y aplicar al algoritmo K-NN
        #print("Clasificación del registro: ")
        #print(registroNC) #registor de prueba procesado para su clasificacion

        NC = registroNC[0] #vector de caracteristicas del registro actual de prueba

        estructuraDatos = {} #inicializacion de la estructura de datos

        for NoCaso, i in enumerate(instancia):
            distancia_NC_i = Canberra(NC, i[0])
            #print(distancia_NC_i)
            estructuraDatos[NoCaso] = distancia_NC_i

        #print(estructuraDatos)  # La distancia de los registros con el registroNC

        ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1] , reverse=False) #ordena los registros
        #de menor a mayor de acuerdo con la distancia con el registroNC
        #print(ordenado)
        j=0
        temporalK = []
        for j in range(k):
            NoCaso = ordenado[j][0]
            #print(etiqueta)
            registro = instancia[NoCaso]
            #print(registro)
            temporalK.append(registro[1]) #obtencion de la etiqueta

        #print("Clases de los vectores más cercanos al registro NC:")
        #print(temporalK)  #los primeros K vectores
        #print("\n\n")


        from statistics import multimode  #<<<- realizado unicamente para fines academicos, no se recomienda poner la importacion aqui
        moda = multimode(temporalK)
        respKnn = moda[0]  # si existe más de una moda se queda con la primera de ellas

        #print("Clase asignada por el KNN: "  + str(respKnn))
        #print("Clase Real: " + registroNC[1])

        if str(respKnn) == registroNC[1]:
            contAciertos += 1


    if(contAciertos/len(prueba)*100>=rendimiento):
        rendimiento=contAciertos/len(prueba)*100
        kmejor=k
        aciertos=contAciertos

print("Total de aciertos: " + str(aciertos))
print("Total de pruebas: " + str(len(prueba)))
print("Rendimiento: " + str(rendimiento))
print("Mejor K:" + str(kmejor))
#Practica:
#Realizar la aplicación de KNN para el calculo del rendimiento de la técnica utilizando la instancia WINE
#   Consideraciones:
#           *Añadir el código necesario para realizar la busqueda automatizada del valor de K que de mejores resultados
#           *Reportar que valor de K es el mejor y que rendimiento genera
#           *PROBAR OTRAS METRICAS DE SIMILITUD - Mínimo 3
#           *Generar matriz de confusión - no obligatoria.
#           *Reporte con el código y ejecución del programa.