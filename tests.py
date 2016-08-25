from a_star import a_star
from a_star import Node
from graph import Graph
from graph import Edge


g = Graph()
g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")
e = Edge(2,"a","b")
g.add_adge(e)
e = Edge(3,"a","c")
g.add_adge(e)
e = Edge(1,"a","d")
g.add_adge(e)
e = Edge(1,"b","c")
g.add_adge(e)
e = Edge(3,"b","d")
g.add_adge(e)
e = Edge(2,"d","c")
g.add_adge(e)


n = Node("a")

r = a_star(g, n)
print("aaaaaaaaaa")
for n in r.lista:
    print(n.vertex, n.get_f())
    if n.parent:
        print(n.parent.vertex, "parent of",n.vertex)
