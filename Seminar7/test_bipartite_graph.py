import unittest
from bipartite_graph import Solution

class TestBipartiteGraph(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_graph(self):
        self.assertTrue(self.solution.is_bipartite([]))

    def test_single_node(self):
        self.assertTrue(self.solution.is_bipartite([[]]))

    def test_two_nodes_connected(self):
        self.assertTrue(self.solution.is_bipartite([[1], [0]]))

    def test_two_nodes_disconnected(self):
        self.assertTrue(self.solution.is_bipartite([[], []]))

    def test_bipartite_cases(self):
        test_cases = [
            ([[1,3], [0,2], [1,3], [0,2]], True),
            ([[1,2,3], [0,2], [0,1,3], [0,2]], False),
            ([[1], [0,2], [1,3], [2]], True),
            ([[1], [0,2], [1,3], [2,4], [3]], True),
            ([[1,2], [0,3], [0,3], [1,2]], True),
        ]
        
        for graph, expected in test_cases:
            with self.subTest(graph=graph):
                self.assertEqual(self.solution.is_bipartite(graph), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)