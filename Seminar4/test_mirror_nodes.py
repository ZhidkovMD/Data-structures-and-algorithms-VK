import unittest
from mirror_nodes import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.count_mirror_nodes(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.count_mirror_nodes(root), 0)

    def test_mirror_pair(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        self.assertEqual(self.solution.count_mirror_nodes(root), 2)

    def test_non_mirror_pair(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.count_mirror_nodes(root), 0)

    def test_complex_mirror(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(3)
        self.assertEqual(self.solution.count_mirror_nodes(root), 4)

    def test_partial_mirror(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.right.right = TreeNode(3)
        self.assertEqual(self.solution.count_mirror_nodes(root), 4)

    def test_deep_mirror(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        self.assertEqual(self.solution.count_mirror_nodes(root), 6)


if __name__ == '__main__':
    unittest.main()