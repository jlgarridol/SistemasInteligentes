'''Clases necesarias para el funcionamiento de los algoritmos'''

class Nodo(object):
    '''Nodo del grafo de búsqueda'''

    def __init__(self, estado, padre):
        '''Crea un nodo, estado hace referencia el estado que representa
           padre al nodo padre'''
        self.estado = estado
        self.padre = padre

    def camino(self):
        '''Devuelve el camino para llegar a este punto'''
        nodo = self
        camino = []
        while nodo:
            camino.append(nodo)
            nodo = nodo.padre
        cad = "Para llegar a la solución el camino es:\n"
        cad += str(camino[-1])
        i = len(camino)-2
        while i >= 0:
            cad += str(camino[i])
            i -= 1
        return cad

    def __eq__(self, nodo):
        '''Desimos que dos nodos son distintos si el estado es distinto'''
        return hash(nodo.estado) == hash(self.estado)


class NodoEstrella(Nodo):
    pass

class NodoJuego(Nodo):
    pass

class Estado(object):
    pass
