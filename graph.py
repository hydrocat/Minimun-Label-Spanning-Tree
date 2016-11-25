class Graph(object):
    """
    n_vertices numero de vertices
    n_label numero de labels. Labels validos 0..(n_label)-1
    """
    def __init__(self, graph, n_vertex, n_label):
        self.graph = graph
        self.n_vertex = n_vertex
        self.n_label = n_label
        self.sets = self.generate_sets()

    def generate_sets(self):
        g = self.graph
        d =dict()
        for v1 in g:
            #print("v1 {}".format(v1))
            for v2 in g[v1]:
                #print("\tv2 {}".format(v2))
                #print("\t   label {}".format(g[v1][v2]))
                try:
                    d[g[v1][v2]].update({v1,v2})
                except KeyError:
                    d[g[v1][v2]] = set()
                    d[g[v1][v2]].update({v1,v2})
        return d

    def remove_label( label ):
        g = self.graph
        for v1 in g:
            for v2 in g[v1]:
                if g[v1][v2] == label:
                    g[v1][v2].pop(label)
            if len(g[v1]) == 0:
                g.pop(v1)
        

