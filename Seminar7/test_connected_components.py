import unittest
from connected_components import Solution


class TestConnectedComponents(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_graph(self):
        self.assertEqual(self.solution.count_components(0, []), 0)

    def test_no_edges(self):
        self.assertEqual(self.solution.count_components(5, []), 5)

    def test_single_node(self):
        self.assertEqual(self.solution.count_components(1, []), 1)

    def test_typical_cases(self):
        test_cases = [
            (5, [[0, 1], [1, 2], [3, 4]], 2),
            (4, [[0, 1], [2, 3], [1, 2]], 1),
            (6, [[0, 1], [1, 2], [4, 5]], 3),
            (3, [[0, 1], [1, 2], [0, 2]], 1),
        ]
        
        for n, edges, expected in test_cases:
            with self.subTest(n=n, edges=edges):
                self.assertEqual(self.solution.count_components(n, edges), expected)

    def test_large_graph(self):
        n = 10000
        edges = [[i, i+1] for i in range(n-1)]
        self.assertEqual(self.solution.count_components(n, edges), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)