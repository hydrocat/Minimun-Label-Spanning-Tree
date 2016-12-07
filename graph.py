class GraphError(Exception):
    """Base class for errors in this module"""
    pass

class SetOnlyGraph(GraphError):
    """Raised when the graph doesn't contain the structure
    of a graph but only the Label-Vertex dictionary representation"""
    def __init__(self):
        self.message = "Graph only have Label-Vertex representation"
        print( self.message )
        
class Graph(object):
    """
    n_vertices numero de vertices
    n_label numero de labels. Labels validos 0..(n_label)-1
    """
    def __init__(self, graph, vertexes, labels, edges, sets = None):
        self.graph = graph
        self.vertexes = vertexes
        self.edges = edges
        self.labels = labels
        self.n_vertex = len(vertexes)
        self.n_label = len(labels)
        if sets == None:
            self.sets = self.generate_sets()
            #self.vertexes = list(range(self.n_vertex))
        else:
            self.graph = None
            self.sets = sets
            #self.vertexes = reduce(lambda acc,x: x.union(acc),
            #                       self.sets)
            
    def filhos(self):
        return self.sons()
    
    def sons(self):
        #let sets be a dictionary in the format:
        #{label:set of accessible vertexes}
        sets = self.sets

        #let labels be all the labels of this Graph
        labels = sets.keys()

        for label in labels:
            #remove the label "label"
            #let ver
            vertexes = sets.pop(label)
            #if all vertexes are still accessible
            if (len(reduce(lambda ac,x: x.union(ac),sets.values())) == self.n_vertex) and (self.connected()):
                #print("Removendo label "+ str(label))
                #remove the unused edges
                new_edge_list = [x for x in self.edges if x[1] != label]
                #yield a new graph
                yield Graph(None,
                            self.vertexes,
                            list(labels),
                            new_edge_list,
                            sets = sets.copy())
            #add the label back to the list
            sets[label] = vertexes

    def generate_sets(self):
        if self.graph == None:
            raise SetOnlyGraph
            return 
        g = self.graph
        d =dict()
        for v1 in g:
            for v2 in g[v1]:
                try:
                    d[g[v1][v2]].update({v1,v2})
                except KeyError:
                    d[g[v1][v2]] = set()
                    d[g[v1][v2]].update({v1,v2})
        d.pop(self.n_label)
        return d
    
    def adj(self, v, vertexes):
        result = []
        for edge in self.edges:
            if edge[0] == v[1]:
                result.extend(
                    filter(
                        lambda x: True if x[1] == edge[2] else False,
                        vertexes))
            elif edge[2] == v[1]:
                result.extend(
                    filter(
                        lambda x: True if x[1] == edge[0] else False,
                        vertexes))
        return result
                
    def connected(self):
            
        #[ g.connected() for g in graph_list ]
        #Modified Deph First
        vertexes = [ ['w',v] for v in self.vertexes ] # w of White
        vertex = vertexes[0] #choose any vertex of the graph

        count = 0
        to_visit = [vertex]
        while len(to_visit) > 0: #is there someone to visit ?
            v = to_visit.pop()
            if v[0] == 'w':
                v[0] = 'b' #black
                count += 1
                to_visit.extend(self.adj(v, vertexes))

        return count == self.n_vertex
        
    def remove_label( label ):
        if self.graph == None:
            print("Grafo sem grafo mas com conjunto de vertices")
            return 
        g = self.graph
        for v1 in g:
            for v2 in g[v1]:
                if g[v1][v2] == label:
                    g[v1][v2].pop(label)
            if len(g[v1]) == 0:
                g.pop(v1)
        
    def __repr__(self):
        return "Grafo com %d labels e %d vertices" % (len(self.sets), self.n_vertex)

    def __eq__(self,other):
        return (self.sets == other.sets)

    def __hash__(self):
        return hash(frozenset(self.sets))

    def __ne__(self,other):
        return (self.sets != other.sets)

    
