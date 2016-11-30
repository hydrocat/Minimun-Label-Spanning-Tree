import unittest
from graph_importer import *

class Test_graph_importer(unittest.TestCase):
    
    def test_import(self):
        graph_reader = Graph_importer("graphs/MDGraph20_20.txt")
        print(read_graph_line("graphs/MDGraph20_20.txt"))
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
            

