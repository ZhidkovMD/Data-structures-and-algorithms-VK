import unittest
from kth_smallest_element_in_bst import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.kth_smallest(None, 1), -1)

    def test_single_node(self):
        root = TreeNode(5)
        self.assertEqual(self.solution.kth_smallest(root, 1), 5)

    def test_small_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(self.solution.kth_smallest(root, 1), 1)
        self.assertEqual(self.solution.kth_smallest(root, 2), 2)
        self.assertEqual(self.solution.kth_smallest(root, 3), 3)
        self.assertEqual(self.solution.kth_smallest(root, 4), 4)

    def test_larger_tree(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(8)
        self.assertEqual(self.solution.kth_smallest(root, 3), 4)
        self.assertEqual(self.solution.kth_smallest(root, 5), 6)

    def test_k_out_of_range(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        self.assertEqual(self.solution.kth_smallest(root, 3), -1)


if __name__ == '__main__':
    unittest.main()