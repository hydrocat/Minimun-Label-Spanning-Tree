from graph import *

def _to_int_list_(string, reverse=False):
    pre = string.strip().split()
    if reverse:
        pre.reverse()
    return map(lambda x: int(x), pre )

def _read_graph_( file ):
    for line in file:
        if line == "\r\n":
            break
        else:
            yield list(enumerate(_to_int_list_(line)))

class Graph_importer(object):
    """
    arquivo : String com o caminho relativo do arquivo
    """
    def __init__(self, file ):
        self.file_name = file

    def graphs(self):
        f = open( self.file_name )
        n_vertex, n_labels = _to_int_list_(f.readline())
        #print("%d %d") %(n_vertex,n_labels)

        dictionary = dict()
        #10 grafos por arquivo
        for x in range(10):
            d = dict()
            edge_list = []
            labels = []
            vertexes = []
            for vertex in list(enumerate(reversed(list(_read_graph_(f))),start=1)):
                d[vertex[0]] = dict()
                for v, label in vertex[1]:
                    d[vertex[0]][v] = label

                    if label != n_labels:
                        edge_list.append( (vertex[0], label, v) )
            #print(len(d))
            yield Graph(d, range(n_vertex), range(n_labels), edge_list )
