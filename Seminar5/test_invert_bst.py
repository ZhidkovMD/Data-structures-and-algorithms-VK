import unittest
from invert_bst import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertIsNone(self.solution.invert_tree(None))

    def test_single_node(self):
        root = TreeNode(1)
        inverted = self.solution.invert_tree(root)
        self.assertEqual(inverted.val, 1)
        self.assertIsNone(inverted.left)
        self.assertIsNone(inverted.right)

    def test_complete_tree(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        inverted = self.solution.invert_tree(root)

        self.assertEqual(inverted.val, 4)
        self.assertEqual(inverted.left.val, 7)
        self.assertEqual(inverted.right.val, 2)
        self.assertEqual(inverted.left.left.val, 9)
        self.assertEqual(inverted.left.right.val, 6)
        self.assertEqual(inverted.right.left.val, 3)
        self.assertEqual(inverted.right.right.val, 1)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)

        inverted = self.solution.invert_tree(root)

        self.assertEqual(inverted.val, 1)
        self.assertIsNone(inverted.left)
        self.assertEqual(inverted.right.val, 2)
        self.assertIsNone(inverted.right.left)
        self.assertEqual(inverted.right.right.val, 3)


if __name__ == '__main__':
    unittest.main()