#arquivo proncipal do projeto
class Heuristica:
    pass


class Node(object):
    def __init__(x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0

    def get_f(self):
        self.f = self.g + self.h
        return self.f



class Mapa:
    def __init__(width, height):
        self.width = width
        self.height = height

        #gera matriz vasia
        self.matrix = [ [0 for _ in range(height)] for _ in range(width)]
        self.nodes = [node() for _ in range(height * width)]
    def reset():
        #limpa o map
        pass


class Lista(object):

    def __init__(self):
        self.lista = []

    def pop(self):
        pass

    def insert(self, node, sort = False):
        #ordena no final?
        self.lista.append(node)
        if sort ==  True:
            self.sort()

    def sort(self):
        #define o elemento a ser usado para ordenação da lista
        def order_element(n):
            return n.get_f()

        sorted(self.lista, key=order_element)

    def print_all():
        for i in self.lista:
            print(i.x, i.y, i.get_f())


def a_pathfinding(from_node, to_node):
    lista_aberta = Lista()
    lista_fechada = Lista()



#
