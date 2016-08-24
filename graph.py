class Edge:
    def __init__(self, weight, vertex_a, vertex_b):
        self.weigth = weigth
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
            return v_counter

    def add_adge(self, edge):
        self.edges.append(edge)
        pass
