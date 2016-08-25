class Edge(object):
    def __init__(self, weight, vertex_a, vertex_b):
        self.weigth = weight
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b

class Graph:
    def __init__(self):
        self.verticeis = []
        self.edges = []
        self.visited = {}

    def add_vertex(self, label):
        if label in self.verticeis:
            return False
        else:
            self.verticeis.append(label)
            self.visited[label] = False

    def set_visited(self, v):
        self.visited[v] = True

    def is_visited_vertex(self, v):
        return self.visited[v]

    def add_adge(self, edge):
        self.edges.append(edge)

    def get_unvisited_edges(self):
        all = []
        for e in self.edges:
            if not (self.visited[e.vertex_a] or self.visited[e.vertex_b]):
                all.append(e)
        return all

    def get_connected_to(self, vertex):
        edges = []
        for e in self.edges:
            if e.vertex_a == vertex or e.vertex_b == vertex:
                edges.append(e)
        return edges

    def get_nearest(self, vertex):
        edge = None
        for e in self.edges:
            if e.vertex_a == vertex or e.vertex_b == vertex:
                if edge is None:
                    edge = e
                if e.weigth < edge.weigth:
                    edge = e
        return edge