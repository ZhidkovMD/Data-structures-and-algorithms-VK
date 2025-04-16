import unittest
from tree_from_array import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        self.assertIsNone(self.solution.array_to_tree([]))
        self.assertIsNone(self.solution.array_to_tree([None]))

    def test_single_node(self):
        root = self.solution.array_to_tree([1])
        self.assertEqual(root.val, 1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_complete_tree(self):
        root = self.solution.array_to_tree([1, 2, 3])
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)

    def test_unbalanced_tree(self):
        root = self.solution.array_to_tree([1, 2, None, 3])
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertIsNone(root.right)
        self.assertEqual(root.left.left.val, 3)

    def test_tree_with_nulls(self):
        root = self.solution.array_to_tree([1, None, 2, None, None, 3])
        self.assertEqual(root.val, 1)
        self.assertIsNone(root.left)
        self.assertEqual(root.right.val, 2)

    def test_complex_tree(self):
        nums = [5, 3, 6, 2, 4, None, None, 1]
        root = self.solution.array_to_tree(nums)
        self.assertEqual(root.val, 5)
        self.assertEqual(root.left.val, 3)
        self.assertEqual(root.right.val, 6)
        self.assertEqual(root.left.left.val, 2)
        self.assertEqual(root.left.right.val, 4)
        self.assertEqual(root.left.left.left.val, 1)


if __name__ == '__main__':
    unittest.main()