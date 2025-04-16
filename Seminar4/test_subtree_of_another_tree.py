import unittest
from subtree_of_another_tree import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_subtree(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.is_subtree(root, None))

    def test_empty_tree(self):
        sub_root = TreeNode(1)
        self.assertFalse(self.solution.is_subtree(None, sub_root))

    def test_single_node_match(self):
        root = TreeNode(1)
        sub_root = TreeNode(1)
        self.assertTrue(self.solution.is_subtree(root, sub_root))

    def test_single_node_mismatch(self):
        root = TreeNode(1)
        sub_root = TreeNode(2)
        self.assertFalse(self.solution.is_subtree(root, sub_root))

    def test_complex_tree_match(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)

        sub_root = TreeNode(4)
        sub_root.left = TreeNode(1)
        sub_root.right = TreeNode(2)

        self.assertTrue(self.solution.is_subtree(root, sub_root))

    def test_complex_tree_mismatch(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)

        sub_root = TreeNode(4)
        sub_root.left = TreeNode(1)
        sub_root.right = TreeNode(3)

        self.assertFalse(self.solution.is_subtree(root, sub_root))


if __name__ == '__main__':
    unittest.main()