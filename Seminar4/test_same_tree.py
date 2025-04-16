import unittest
from same_tree import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def test_both_trees_empty(self):
        solution = Solution()
        self.assertTrue(solution.is_same_tree(None, None))

    def test_one_tree_empty(self):
        solution = Solution()
        tree = TreeNode(1)
        self.assertFalse(solution.is_same_tree(tree, None))
        self.assertFalse(solution.is_same_tree(None, tree))

    def test_identical_single_node_trees(self):
        tree1 = TreeNode(1)
        tree2 = TreeNode(1)
        solution = Solution()
        self.assertTrue(solution.is_same_tree(tree1, tree2))

    def test_different_single_node_trees(self):
        tree1 = TreeNode(1)
        tree2 = TreeNode(2)
        solution = Solution()
        self.assertFalse(solution.is_same_tree(tree1, tree2))

    def test_identical_multi_node_trees(self):
        tree1 = TreeNode(1)
        tree1.left = TreeNode(2)
        tree1.right = TreeNode(3)
        
        tree2 = TreeNode(1)
        tree2.left = TreeNode(2)
        tree2.right = TreeNode(3)
        
        solution = Solution()
        self.assertTrue(solution.is_same_tree(tree1, tree2))

    def test_different_multi_node_trees(self):
        tree1 = TreeNode(1)
        tree1.left = TreeNode(2)
        tree1.right = TreeNode(3)
        
        tree2 = TreeNode(1)
        tree2.left = TreeNode(3)
        tree2.right = TreeNode(2)
        
        solution = Solution()
        self.assertFalse(solution.is_same_tree(tree1, tree2))


if __name__ == '__main__':
    unittest.main()