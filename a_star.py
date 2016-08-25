#arquivo proncipal do projeto

# from kruskal import Kruskal
# from graph import Graph
# from graph import Edge

class Node(object):
    def __init__(self, v, parent=None):
        self.vertex = v
        self.g = 0
        self.h = 0
        self.parent = parent

    def get_f(self):
        return self.g + self.h

class Lista(object):

    def __init__(self, sort = False):
        self.lista = []
        self.sort = sort
    def pop(self):
        return self.lista.pop(0)

    def empty(self):
        return not self.lista

    def insert(self, node):
        #ordena no final?
        self.lista.append(node)

        if self.sort:
            self.sorted()

    def sorted(self):
        #define o elemento a ser usado para ordenação da lista
        def order_element(n):
            return n.get_f()

        self.lista = sorted(self.lista, key=order_element)

    def inlist(self, node):
        for l in self.lista:
            if node.vertex == l.vertex:
                return True
        return False

    def get_node_from_vertex(self):
        return 0

    def print_all(self):
        for i in self.lista:
            print(i.x, i.y, i.get_f())


def a_star(graph_g, from_node):

    def g(node, ec):
        if node.parent is None:
            return ec
        else:
            return node.parent.g + ec


    def h():
        return 0

    lista_aberta = Lista(True)

    lista_fechada = Lista(False)

    from_node.g = g(from_node, 0)
    from_node.h = h()

    lista_aberta.insert(from_node)

    while(lista_aberta.empty() == False):

        n = lista_aberta.pop()

        edges = graph_g.get_connected_to(n.vertex)

        for e in edges:
            edge_cost = 0
            if e.vertex_a == n.vertex:
                nnode = Node(e.vertex_b, n)
                edge_cost = e.weigth
            elif e.vertex_b == n.vertex:
                edge_cost = e.weigth
                nnode = Node(e.vertex_a, n)

            # se estiver na lista fechada não sera computado novamente
            if lista_fechada.inlist(nnode) == False:
                # se estiver na lista aberta podera ser reparenteado
                if lista_aberta.inlist(nnode):
                    if nnode.get_f() < lista_fechada.get_node_from_vertex():
                        pass
                else:
                    nnode.g = g(nnode, edge_cost)
                    nnode.h = h()
                    lista_aberta.insert(nnode)
        lista_fechada.insert(n)
    return lista_fechada


#
