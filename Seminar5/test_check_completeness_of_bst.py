import unittest
from check_completeness_of_bst import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertTrue(self.solution.is_complete_tree(None))

    def test_single_node(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.is_complete_tree(root))

    def test_complete_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertTrue(self.solution.is_complete_tree(root))

    def test_incomplete_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        self.assertFalse(self.solution.is_complete_tree(root))

    def test_complete_tree_with_null_right(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertTrue(self.solution.is_complete_tree(root))

    def test_incomplete_tree_with_gap(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        self.assertFalse(self.solution.is_complete_tree(root))


if __name__ == '__main__':
    unittest.main()