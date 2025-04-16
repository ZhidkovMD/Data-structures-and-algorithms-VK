import unittest
from min_depth_of_bst import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def test_empty_tree(self):
        solution = Solution()
        self.assertEqual(solution.min_depth(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        solution = Solution()
        self.assertEqual(solution.min_depth(root), 1)

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        solution = Solution()
        self.assertEqual(solution.min_depth(root), 2)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        solution = Solution()
        self.assertEqual(solution.min_depth(root), 3)

    def test_left_heavy_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        solution = Solution()
        self.assertEqual(solution.min_depth(root), 2)

    def test_right_heavy_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)
        solution = Solution()
        self.assertEqual(solution.min_depth(root), 2)


if __name__ == '__main__':
    unittest.main()