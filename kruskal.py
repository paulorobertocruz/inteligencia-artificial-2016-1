class DisjointSets:
    def __init__(self):
        self.parents = {}
        self.sets = {}
        self.ranks = {}

    def find(self, set):
        if self.parents[set] == set:
            return set
        else:
            return find(parents[set])

    def union(self, set_a, set_b):
        if ranks[set_a] > ranks[set_b]:
            parents[set_a] = set_b
        elif ranks[set_b] > ranks[set_a]:
            parents[set_b] = set_a
        else:
            parents[set_a] = set_b
            ranks[set_b]+= 1
