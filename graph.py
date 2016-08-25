class Edge(object):
    def __init__(self, weight, vertex_a, vertex_b):
        self.weigth = weight
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b

class Graph:
    def __init__(self):
        self.verticeis = []
        self.edges = []

    def add_vertex(self, label):
        if label in self.verticeis:
            return False
        else:
            self.verticeis.append(label)

    def add_adge(self, edge):
        self.edges.append(edge)

    def get_connected_to(self, vertex):
        edges = []
        for e in self.edges:
            if e.vertex_a == vertex or e.vertex_b == vertex:
                edges.append(e)
        return edges
