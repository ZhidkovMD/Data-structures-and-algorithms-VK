import unittest
from typing import List, Dict, Tuple
from dijkstra_algorithm import Solution

class TestDijkstraAlgorithm(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_single_node(self):
        edges = [[]]
        result = self.solution.dijkstra(1, edges, 0)
        self.assertEqual(result, {0: 0})

    def test_disconnected_nodes(self):
        edges = [[], []]
        result = self.solution.dijkstra(2, edges, 0)
        self.assertEqual(result, {0: 0, 1: float('inf')})

    def test_start_node_out_of_range(self):
        edges = [[(1, 5)], [(0, 5)]]
        with self.assertRaises(IndexError):
            self.solution.dijkstra(2, edges, 2)

    def test_shortest_path_cases(self):
        test_cases = [
            (
                3, 
                [[(1, 1), (2, 4)], [(0, 1), (2, 2)], [(0, 4), (1, 2)]],
                0,
                {0: 0, 1: 1, 2: 3}
            ),
            (
                5,
                [[(1, 4), (2, 1)], [(0, 4), (2, 2), (3, 1)], [(0, 1), (1, 2), (3, 5)], [(1, 1), (2, 5), (4, 3)], [(3, 3)]],
                0,
                {0: 0, 1: 3, 2: 1, 3: 4, 4: 7}
            ),
            (
                4,
                [[(1, 1), (2, 1), (3, 1)], [(0, 1)], [(0, 1)], [(0, 1)]],
                0,
                {0: 0, 1: 1, 2: 1, 3: 1}
            )
        ]
        
        for n, edges, start, expected in test_cases:
            with self.subTest(n=n, start=start):
                result = self.solution.dijkstra(n, edges, start)
                self.assertEqual(result, expected)

    def test_large_graph(self):
        n = 1000
        edges = [[(i+1, 1)] for i in range(n-1)] + [[]]
        result = self.solution.dijkstra(n, edges, 0)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[500], 500)
        self.assertEqual(result[999], 999)

if __name__ == "__main__":
    unittest.main(verbosity=2)