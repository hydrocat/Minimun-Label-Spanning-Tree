from graph_importer import *

graph_importer = Graph_importer("graphs/LDGraph50_12.txt")
graph_list = list(graph_importer.graphs())
print(len(graph_list))
graph = graph_list[0]
print(graph.sets[12])
