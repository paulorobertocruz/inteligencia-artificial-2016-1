#arquivo proncipal do projeto

from kruskal import Kruskal_Unvisited
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
                return l
        return None

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


    def h(node):
        hc = 0

        edges = graph_g.get_connected_to(node.vertex)

        neares_cost = None
        print(node.vertex)
        for e in edges:
            if e.vertex_a == node.vertex:
                nv = graph_g.is_visited_vertex(e.vertex_b)
            else:
                nv = graph_g.is_visited_vertex(e.vertex_a)

            if nv:
                #ja foi visitada
                continue
            else:
                #não foi visitada
                neares_cost = e.weigth
        print(neares_cost)
        hc = hc + neares_cost
        mst = Kruskal_Unvisited(graph_g)
        mst_cost = 0

        for e in mst:
            mst_cost += e.weigth

        hc += mst_cost
        return hc

    lista_aberta = Lista(True)

    lista_fechada = Lista(False)

    from_node.g = g(from_node, 0)
    from_node.h = h(from_node)

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

            nnode.g = g(nnode, edge_cost)
            nnode.h = h(nnode)

            # se estiver na lista fechada não sera computado novamente
            if lista_fechada.inlist(nnode) is None:
                # se estiver na lista aberta podera ser reparenteado
                list_node = lista_aberta.inlist(nnode)
                if list_node is not None:
                    if nnode.get_f() < list_node.get_f():
                        list_node.parent = nnode.parent
                        list_node.g = nnode.g
                        list_node.h = nnode.h
                else:
                    lista_aberta.insert(nnode)
        lista_fechada.insert(n)
        graph_g.set_visited(n.vertex)
    return lista_fechada


#
