import .graph

class DisjointSets:
    def __init__(self):
        #gr graph
        self.parent = {}
        self.set = {}
        self.rank = {}

    def add_set(self, v):
        self.set.append(v)
        self.parent[v]=v
        self.rank[v]=0

    def find(self, set):
        if self.parent[set] == set:
            return set
        else:
            return find(parent[set])

    def union(self, set_a, set_b):
        if rank[set_a] > rank[set_b]:
            parent[set_a] = set_b
        elif rank[set_b] > rank[set_a]:
            parent[set_b] = set_a
        else:
            parent[set_a] = set_b
            rank[set_b]+= 1

def kruskal(gr):
    #lista de arestas da mst
    mst_adges = []

    dis_set = DisjointSets()

    for v in gr.verticeis:
        dis_set.set(v)
    #ordena todas as arestas em order crescente
    def order_element(edge):
        return edge.weigth
    all_edges = sorted(gr.edges, key=order_element)

    for e in all_edges:
        if dis_set.find(e.vertex_a) != dis_set.find(e.vertex_b):
            mst_adges.append(e)
            dis_set.union(e.vertex_a, e.vertex_b)
    return mst_adges








#
