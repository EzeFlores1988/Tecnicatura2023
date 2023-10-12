#DEFINIR UNA TUPLA
print("Definir una tupla")
cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)
print()

#CANTIDAD DE ELEMENTOS DE LA TUPLA
print("la cantidad de elementos")
print(len(cocina))
print()

#ACCEDER A UN ELEMENTO DE LA TUPLA
print(cocina[1])
print()

#ACCERDER DE MANERA INVERSA
print("ultimo elemento ubicado en la tupla")
print(cocina[-1])
print()

#ACCEDER A UN RANGO
print(cocina[0:1])
print(cocina[0:2])

#EJEMPLO
verdura = ("papa",) #SE NECESITA LA COMA PARA QUE SEA UNA TUPLA
#DE LO CONTRARIO SOLO SERIA UN TIPO STRING(CADENA)

print()

#RECORRER LOS ELEMENTOS DE LA TUPLA
for cocinar in cocina:
    print(cocinar, end=' ') #Usa los saltos de linea para negar eso se usa el end=''
print()

#NO SE PUEDE AGREGAR ELEMENTOS (MODIFICACIONES) A LA TUPLA ENTONCES SE GENERA UNA CONVERSION DEL MISMO
#MODIFICAR DE TUPLA A LISTA a LISTA A TUPLA
#NO ES BUENA PRACTICA HACER ESTE TIPO DE CONVERSIONES.
cocinaLista = list(cocina)
cocinaLista[0] = "Vaso"
cocina = tuple(cocinaLista)
print('\n', cocina)
print()

"""
#ELIMINAR LA TUPLA
del cocina
print(cocina)
"""

#EJERCICIO DE TUPLA
#DADA LA SIGUIENTE TUPLA
tupla = (13, 1, 8, 3, 2, 5, 8)
#definimos la tupla
#crear una lista que solo incluya los numeros menores a 5 e imprima por consola [1, 3, 2]

lista = [] #SE DEFINE LA LISTA Y SE FILTRA LOS ELEMENTOS MENORES A 5 DE LA TUPLA
for elementos in tupla:
    if elementos < 5:
        lista.append(elementos)
print(lista)
