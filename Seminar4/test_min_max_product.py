import unittest
from min_max_product import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.min_dot_max(None), 0)

    def test_single_node(self):
        root = TreeNode(5)
        self.assertEqual(self.solution.min_dot_max(root), 25)

    def test_positive_numbers(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.right.right = TreeNode(20)
        self.assertEqual(self.solution.min_dot_max(root), 60)

    def test_negative_numbers(self):
        root = TreeNode(-5)
        root.left = TreeNode(-10)
        root.right = TreeNode(-3)
        self.assertEqual(self.solution.min_dot_max(root), 30)

    def test_mixed_numbers(self):
        root = TreeNode(0)
        root.left = TreeNode(-5)
        root.right = TreeNode(10)
        self.assertEqual(self.solution.min_dot_max(root), -50)

    def test_large_tree(self):
        root = TreeNode(100)
        root.left = TreeNode(50)
        root.right = TreeNode(150)
        root.left.left = TreeNode(25)
        root.left.right = TreeNode(75)
        root.right.left = TreeNode(125)
        root.right.right = TreeNode(200)
        root.left.left.left = TreeNode(10)
        root.right.right.right = TreeNode(300)
        self.assertEqual(self.solution.min_dot_max(root), 3000)


if __name__ == '__main__':
    unittest.main()