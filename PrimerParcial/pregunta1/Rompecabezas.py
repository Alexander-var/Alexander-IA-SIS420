from busquedas_02 import aestrella, ProblemaBusqueda

# Elaborar un agente que resuelva un rompecabezas de 4x3  4 filas y 3 colunas
OBJETIVO = """1-2-3
4-5-6
7-8-9
a-b-e"""
INICIAL = '''e-1-2
3-4-5
8-9-6
7-a-b'''


#INICIAL = """1-2-3
#4-5-6
#7-8-9
#a-e-b"""



def list_to_string(list_):
    return "\n".join(["-".join(row) for row in list_])


def string_to_list(string_):
    return [row.split("-") for row in string_.split("\n")]


def find_location(filas, element_to_find):
    """Encuentra la ubicacion de una pieza en el rompecabezas.
    DEvuelve una tupla: fila, columna"""
    for ir, row in enumerate(filas):
        for ic, element in enumerate(row):
            if element == element_to_find:
                #print(element)
                return ir, ic


posiciones_objetivo = {}
filas_objetivo = string_to_list(OBJETIVO)

for numero in "123456789abe":
    posiciones_objetivo[numero] = find_location(filas_objetivo, numero)


class EigthPuzzleProblem(ProblemaBusqueda):
    def acciones(self, estado):
        """Devuelve una lista de piesas que se pueden mover a un espacio vacio."""
        filas = string_to_list(estado)
        fila_e, columna_e = find_location(filas, "e")

        acciones = []
        if fila_e > 0:
            acciones.append(filas[fila_e - 1][columna_e])
        if fila_e < 3:
            acciones.append(filas[fila_e + 1][columna_e])
        if columna_e > 0:
            acciones.append(filas[fila_e][columna_e - 1])
        if columna_e < 2:
            acciones.append(filas[fila_e][columna_e + 1])

        return acciones

    def resultado(self, estado, accion):
        """Devuelve el resultado despues de mover una pieza a un espacio en vacio"""
        filas = string_to_list(estado)
        fila_e, columna_e = find_location(filas, "e")
        fila_n, columna_n = find_location(filas, accion)

        filas[fila_e][columna_e], filas[fila_n][columna_n] = (
            filas[fila_n][columna_n],
            filas[fila_e][columna_e],
        )

        return list_to_string(filas)

    def es_objetivo(self, estado):
        """Devuelve True si un estado es el estado_objetivo."""
        return estado == OBJETIVO

    def costo(self, estado1, accion, estado2):
        """Devuelve el costo de ejecutar una accion."""
        return 1

    def heuristica(self, estado):
        """Devuelve una estimacion de la distancia
        de un estado a otro, utilizando la distancia manhattan.
        """
        matriz = string_to_list(estado)
        distancia = 0
        for numero in "123456789abe":
            # indice actual
            fila_n, columna_n = find_location(matriz, numero)
            # indice objetivo
            fila_n_objetivo, col_n_goal = posiciones_objetivo[numero]

            distancia += abs(fila_n - fila_n_objetivo) + abs(columna_n - col_n_goal)
        return distancia


resultado = aestrella(EigthPuzzleProblem(INICIAL))

for accion, estado in resultado.camino():
    print("Move numero", accion)
    print(estado)
