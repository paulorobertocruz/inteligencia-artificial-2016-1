#arquivo proncipal do projeto

from kruskal import Kruskal
from graph import Graph
from graph import Edge

class Node(object):
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0

    def get_f(self):
        return self.g + self.h

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

        self.lista = sorted(self.lista, key=order_element)

    def print_all(self):
        for i in self.lista:
            print(i.x, i.y, i.get_f())


def a_pathfinding(from_node, to_node):
    lista_aberta = Lista()
    lista_fechada = Lista()


#
