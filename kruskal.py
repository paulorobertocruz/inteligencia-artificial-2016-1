import graph

class DisjointSets:
    def __init__(self):
        #gr graph
        self.parent = {}
        self.set = []
        self.rank = {}

    def add_set(self, v):
        self.set.append(v)
        self.parent[v] = v
        self.rank[v]=0

    def find(self, set):
        if self.parent[set] == set:
            return self.parent[set]
        else:
            return self.find(self.parent[set])
    def set_exist(self, set):
        if set in self.parent:
            return True
        else:
            return False

    def union(self, set_a, set_b):
        ra = self.find(set_a)
        rb = self.find(set_b)
        if self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        elif self.rank[rb] > self.rank[ra]:
            self.parent[ra] = rb
        else:
            self.parent[ra] = rb
            self.rank[rb]+= 1

def Kruskal(gr):
    #lista de arestas da mst
    mst_adges = []

    dis_set = DisjointSets()

    for v in gr.verticeis:
        dis_set.add_set(v)

    #ordena todas as arestas em order crescente
    def order_element(edge):
        return edge.weigth

    all_edges = sorted(gr.edges, key=order_element)

    for e in all_edges:
        if dis_set.find(e.vertex_a) != dis_set.find(e.vertex_b):
            mst_adges.append(e)
            dis_set.union(e.vertex_a, e.vertex_b)
    return mst_adges

def Kruskal_Unvisited(gr):
    #lista de arestas da mst
    mst_adges = []

    dis_set = DisjointSets()

    for v in gr.verticeis:
        if not gr.is_visited_vertex(v):
            dis_set.add_set(v)

    #ordena todas as arestas em order crescente
    def order_element(edge):
        return edge.weigth

    all_edges = sorted(gr.get_unvisited_edges(), key=order_element)

    for e in all_edges:
        if dis_set.find(e.vertex_a) != dis_set.find(e.vertex_b):
            mst_adges.append(e)
            dis_set.union(e.vertex_a, e.vertex_b)
    return mst_adges








#
