import graph as g
from graph_importer import *
from connected_component import *
from heuristicas import *

graph_importer = Graph_importer("graphs/LDGraph50_12.txt")
graph_list = graph_importer.graphs()
graph_list = list(graph_list)

graph = graph_list[1]
sl = [graph]
while len(sl) > 0:
    candidato = sl.pop()
    filhos = list(candidato.filhos())
    if len(filhos) == 0:
        print candidato
        print label_amount(candidato)
    else:
        for x in filhos:
            sl.append(x)


