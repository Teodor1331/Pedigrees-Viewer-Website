import unittest
import networkx as nx

from ExerciseNetworkX import graph1, graph2, graph3

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7], list(graph1.nodes))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7], list(graph2.nodes))

        self.assertEqual([(0, 1), (0, 3), (1, 6), (2, 0), (3, 1), (3, 7), (4, 2), (5, 1), (6, 4), (7, 6)], list(graph1.edges))
        self.assertEqual([(0, 1), (0, 3), (1, 3), (1, 5), (2, 0), (2, 1), (3, 7), (4, 7), (5, 1), (5, 7), (6, 2), (6, 4)], list(graph2.edges))
        self.assertEqual([0, 1, 2, 3, 4, 5], list(graph3.nodes))

        self.assertEqual([(0, 1), (1, 6), (6, 4), (4, 2), (0, 3), (3, 7)], list(nx.dfs_edges(graph1, source = 0)))
        self.assertEqual([(0, 1), (0, 3), (1, 5), (3, 7)], list(nx.bfs_edges(graph2, source = 0)))
        self.assertEqual([0, 2, 5], nx.dijkstra_path(graph3, 0, 5))
        self.assertEqual(11, nx.dijkstra_path_length(graph3, 0, 5))


if __name__ == "__main__":
    unittest.main()