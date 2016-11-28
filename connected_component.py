from copy import deepcopy
from graph_importer import *

def connected(graph_list):
    
    for graph in graph_list:

        graph.sets.pop(graph.n_label)
        backup = set.union(*graph.sets.values()[0:])
       # print backup

        for k in graph.sets.keys():
            r = graph.sets.pop(k)

              #  print (len(graph.sets.values()))
                #print graph.sets.values()
             #   set.union(*graph.sets.values()[0:])
            #set.union(*graph.sets.values()[0:])
            if (len(graph.sets.values()) is not 0):
                if (not r.issubset(set.union(*graph.sets.values()[0:]))):
     #                   print "r {}".format(r)
      #                  print "union {}".format(set.union(*graph.sets.values()[0:]))
       #                 print "one time"
                        graph.sets[k] = r
            else:
                print("pqp")
                graph.sets[k] = r
        if not backup.issubset(set.union(*graph.sets.values()[0:])):
            print "foi eliminado"
        else:
            print len(graph.sets)
            print set.union(*graph.sets.values()[0:])
