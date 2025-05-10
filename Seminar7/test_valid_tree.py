import unittest
from typing import List
from valid_tree import Solution

class TestValidTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_graph(self):
        self.assertTrue(self.solution.valid_tree(0, []))

    def test_single_node(self):
        self.assertTrue(self.solution.valid_tree(1, []))

    def test_two_nodes_connected(self):
        self.assertTrue(self.solution.valid_tree(2, [[0, 1]]))

    def test_two_nodes_disconnected(self):
        self.assertFalse(self.solution.valid_tree(2, []))

    def test_tree_cases(self):
        test_cases = [
            (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
            (5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]], False),
            (4, [[0, 1], [2, 3]], False),
            (3, [[0, 1], [1, 2], [2, 0]], False),
            (4, [[0, 1], [1, 2], [1, 3]], True),
        ]
        
        for n, edges, expected in test_cases:
            with self.subTest(n=n, edges=edges):
                self.assertEqual(self.solution.valid_tree(n, edges), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)