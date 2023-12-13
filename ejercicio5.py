##generar n numeros randomicos entre 0 y 50 pares y guardarlos en un vector. Calcular cuantos son menores que el promedio, y si el conteo es menor que la mitad de n, ordenar los numeros menores al promedio. 

import random
import time
from time import time

##start
n=int(input("Digite el valor de n: "))
vector = []


##validating n
while n!=5000 and n!=15000 and n!=30000 and n!=90000000:
    print("El valor de n debe ser 5000, 15000, 30000 o 50000")
    n=int(input("Digite el valor de n: "))

##start time
inicio = time() 
    
#generating random numbers
while len(vector)<n:    
    numero=int(random.uniform(0,11))
    if numero % 2 == 0:
        vector.append(numero)


##print vector
##print(vector)

##calculating average
suma=0
for i in range(len(vector)):
    suma=suma+vector[i]
    
promedio=suma/len(vector)
print("El promedio es: ",promedio)

##calculating how many numbers are less than average
contador=0
for i in range(len(vector)):
    if vector[i]<promedio:
        contador=contador+1
        
print("\nHay ",contador," numeros menores que el promedio")

##sorting numbers less than average if the count is less than half of n usinng quicksort
if contador<(n/2):
    print("Se ordenó el vector con los numeros menores al promedio")
    #creating vector with numbers less than average
    vector2=[]
    for i in range(len(vector)):
        if vector[i]<promedio:
            vector2.append(vector[i])
            
    ##ordenating vector using method quicksort
def quicksort(vector):
    if len(vector) <= 1:
        return vector  # Si la lista tiene 0 o 1 elemento, ya está ordenada.

    # Elegimos un pivote (generalmente el último elemento) y dividimos la lista en tres partes.
    pivot = vector[len(vector) - 1]
    menores = []
    iguales = []
    mayores = []

    for element in vector:
        if element < pivot:
            menores.append(element)
        elif element == pivot:
            iguales.append(element)
        else:
            mayores.append(element)

    # Luego, aplicamos Quicksort de manera recursiva a las sublistas menor y mayor.
    sorted_menores = quicksort(menores)
    sorted_mayores = quicksort(mayores)

    # Finalmente, combinamos las sublistas ordenadas y el pivote igual en una sola lista.
    return sorted_menores + iguales + sorted_mayores

    ##calling function quicksort
    quicksort(vector2)


print("EL tiempo de ejecucion es: ",time()-inicio)

