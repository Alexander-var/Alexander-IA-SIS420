from busquedas_02 import aestrella, ProblemaBusqueda

#OBJETIVO = """1-2-3-a
#4-5-6-b
#7-8-9-c
#d-g-f-e"""

#INICIAL = """2-e-3-a
#1-5-9-6
#4-7-8-b
#d-g-f-c"""

OBJETIVO = """1-2-3-4-a
5-6-7-8-b
9-c-d-f-g
h-i-j-k-l
m-n-o-p-e"""

INICIAL = """1-2-3-4-a
5-6-7-8-b
9-c-d-f-g
h-i-j-k-l
m-n-o-e-p"""

#OBJETIVO = """1-2
#3-e"""

#INICIAL = """3-1
#2-e"""

def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])


def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]


def find_location(filas, element_to_find):
    '''Encuentra la ubicacion de una pieza en el rompecabezas.
       DEvuelve una tupla: fila, columna'''
    for ir, row in enumerate(filas):
        for ic, element in enumerate(row):
            if element == element_to_find:
                #print(element)
                return ir, ic


posiciones_objetivo = {}
filas_objetivo = string_to_list(OBJETIVO)
for numero in "123456789abcdefghijklmnop":
    posiciones_objetivo[numero] = find_location(filas_objetivo, numero)
    #print(numero)
#exit()
class EigthPuzzleProblem(ProblemaBusqueda):
    def acciones(self, estado):
        '''Devuelve una lista de piesas que se pueden mover a un espacio vacio.'''
        filas = string_to_list(estado)
        #print(filas)
        fila_e, columna_e = find_location(filas, 'e')
        #print(fila_e,columna_e)
        acciones = []
        if fila_e > 0:
            acciones.append(filas[fila_e - 1][columna_e])
        if fila_e < 4:
            acciones.append(filas[fila_e + 1][columna_e])
        if columna_e > 0:
            acciones.append(filas[fila_e][columna_e - 1])
        if columna_e < 4:
            acciones.append(filas[fila_e][columna_e + 1])

        return acciones

    def resultado(self, estado, accion):
        '''Devuelve el resultado despues de mover una pieza a un espacio en vacio
        '''
        filas = string_to_list(estado)
        fila_e, columna_e = find_location(filas, 'e')
        fila_n, columna_n = find_location(filas, accion)

        filas[fila_e][columna_e], filas[fila_n][columna_n] = filas[fila_n][columna_n], filas[fila_e][columna_e]

        return list_to_string(filas)

    def es_objetivo(self, estado):
        '''Devuelve True si un estado es el estado_objetivo.'''
        return estado == OBJETIVO

    def costo(self, estado1, accion, estado2):
        '''Devuelve el costo de ejecutar una accion. 
        '''
        return 1

    def heuristica(self, estado):
        '''Devuelve una estimacion de la distancia
        de un estado a otro, utilizando la distancia manhattan.
        '''
        filas = string_to_list(estado)

        distancia = 0

        for numero in "123456789abcdefghijklmnop":
            fila_n, columna_n = find_location(filas, numero)
            fila_n_objetivo, col_n_goal = posiciones_objetivo[numero]

            distancia += abs(fila_n - fila_n_objetivo) + abs(columna_n - col_n_goal)

        return distancia


resultado = aestrella(EigthPuzzleProblem(INICIAL))
for accion, estado in resultado.camino():
    print('Move numero', accion)
    print(estado)

