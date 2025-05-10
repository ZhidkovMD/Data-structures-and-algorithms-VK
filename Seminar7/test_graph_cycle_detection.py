import unittest
from graph_cycle_detection import Solution


class TestGraphCycleDetection(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_graph(self):
        self.assertFalse(self.solution.has_cycle(0, []))

    def test_single_node(self):
        self.assertFalse(self.solution.has_cycle(1, []))

    def test_two_nodes_connected(self):
        self.assertFalse(self.solution.has_cycle(2, [[0, 1]]))

    def test_cycle_cases(self):
        test_cases = [
            (3, [[0, 1], [1, 2], [2, 0]], True),
            (4, [[0, 1], [1, 2], [2, 3]], False),
            (5, [[0, 1], [1, 2], [2, 0], [3, 4]], True),
            (4, [[0, 1], [1, 2], [2, 3], [3, 0]], True),
        ]
        
        for n, edges, expected in test_cases:
            with self.subTest(n=n, edges=edges):
                self.assertEqual(self.solution.has_cycle(n, edges), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)