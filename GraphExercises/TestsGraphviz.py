import unittest

from ExerciseGraphviz import graph1, graph2
from ExerciseGraphviz import list_edges1, list_edges2
from ExerciseGraphviz import list_attributes1, list_attributes2
from ExerciseGraphviz import adjency_list11, adjency_list12, adjency_list21, adjency_list22


class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual("Name Graph DFS", graph1.name)
        self.assertEqual("Name Graph BFS", graph2.name)

        self.assertEqual(['0 -> 1', '0 -> 3', '1 -> 6', '2 -> 0', '3 -> 1', '3 -> 7', '4 -> 2', '5 -> 1', '6 -> 4', '7 -> 6'], list_edges1)
        self.assertEqual(['0 -> 1', '0 -> 3', '1 -> 3', '1 -> 5', '2 -> 0', '2 -> 1', '3 -> 7', '4 -> 7', '5 -> 1', '5 -> 7', '6 -> 2', '6 -> 4'], list_edges2)

        self.assertEqual(adjency_list11, adjency_list12)
        self.assertEqual(adjency_list21, adjency_list22)



if __name__ == "__main__":
    unittest.main()