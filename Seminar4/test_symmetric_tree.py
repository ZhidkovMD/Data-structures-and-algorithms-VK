import unittest
from symmetric_tree import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def test_empty_tree(self):
        solution = Solution()
        self.assertTrue(solution.is_symmetric(None))

    def test_single_node(self):
        root = TreeNode(1)
        solution = Solution()
        self.assertTrue(solution.is_symmetric(root))

    def test_symmetric_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        solution = Solution()
        self.assertTrue(solution.is_symmetric(root))

    def test_asymmetric_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(3)
        solution = Solution()
        self.assertFalse(solution.is_symmetric(root))

    def test_mirror_structure_only(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(3)
        solution = Solution()
        self.assertTrue(solution.is_symmetric(root))

    def test_different_values(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        solution = Solution()
        self.assertFalse(solution.is_symmetric(root))


if __name__ == '__main__':
    unittest.main()