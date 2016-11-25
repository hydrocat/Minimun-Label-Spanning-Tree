from graph import *

def to_int_list(string, reverse=False):
    pre = string.strip().split()
    if reverse:
        pre.reverse()
    return map(lambda x: int(x), pre )

def read_graph( file ):
    for line in file:
        if line == "\r\n":
            break
        else:
            yield list(enumerate(to_int_list(line)))

class Graph_importer(object):
    """
    arquivo : String com o caminho relativo do arquivo
    """
    def __init__(self, file ):
        self.file_name = file

    def graphs(self):
        f = open( self.file_name )
        vertex, labels = to_int_list(f.readline())

        dictionary = dict()
        for x in range(10):
            d = dict()
            for vertex in list(enumerate(reversed(list(read_graph(f))),start=1)):
                d[vertex[0]] = dict()
                for v, label in vertex[1]:
                    d[vertex[0]][v] = label
            yield Graph(d, vertex, labels )

        

        
