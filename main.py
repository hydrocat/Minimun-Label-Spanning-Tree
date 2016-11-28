from graph_importer import *
from connected_component import *

graph_importer = Graph_importer("graphs/LDGraph50_12.txt")
graph_list = list(graph_importer.graphs())
#print(len(graph_list))
graph = graph_list[1]

#print(set.intersection(*graph.sets.values()[8:10]))
#print()
#print(graph.sets)
#print()
print graph.sons()
#connected(graph_list)
