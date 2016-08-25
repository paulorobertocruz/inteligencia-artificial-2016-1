#arquivo proncipal do projeto

from kruskal import Kruskal
from graph import Graph
from graph import Edge

class Node(object):
    def __init__(self, v):
        self.vertex = v
        self.g = 0
        self.h = 0

    def get_f(self):
        return self.g + self.h
    def set_g(self):
        pass
    def set_h(self):
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

        self.lista = sorted(self.lista, key=order_element)

    def print_all(self):
        for i in self.lista:
            print(i.x, i.y, i.get_f())


def a_star(graph_g, from_node):
    lista_aberta = Lista()
    lista_fechada = Lista()


#
