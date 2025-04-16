import unittest
from balance_factor import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertIsNone(self.solution.calculate_balance_factors(None))

    def test_single_node(self):
        root = TreeNode(1)
        self.solution.calculate_balance_factors(root)
        self.assertEqual(root.balance_factor, 0)

    def test_balanced_tree(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.solution.calculate_balance_factors(root)
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, 0)
        self.assertEqual(root.right.balance_factor, 0)

    def test_left_heavy_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        self.solution.calculate_balance_factors(root)
        self.assertEqual(root.balance_factor, 2)
        self.assertEqual(root.left.balance_factor, 1)
        self.assertEqual(root.left.left.balance_factor, 0)

    def test_right_heavy_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.solution.calculate_balance_factors(root)
        self.assertEqual(root.balance_factor, -2)
        self.assertEqual(root.right.balance_factor, -1)
        self.assertEqual(root.right.right.balance_factor, 0)

    def test_complex_tree(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(5)
        self.solution.calculate_balance_factors(root)
        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, 0)
        self.assertEqual(root.right.balance_factor, 1)
        self.assertEqual(root.left.left.balance_factor, 0)
        self.assertEqual(root.left.right.balance_factor, 0)
        self.assertEqual(root.right.left.balance_factor, 0)


if __name__ == '__main__':
    unittest.main()