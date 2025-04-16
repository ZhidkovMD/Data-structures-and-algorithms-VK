from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_dot_max(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.min_val = float('inf')
        self.max_val = float('-inf')

        self._traverse(root)

        return self.min_val * self.max_val

    def _traverse(self, node: Optional[TreeNode]) -> None:
        if not node:
            return

        if node.val < self.min_val:
            self.min_val = node.val
        if node.val > self.max_val:
            self.max_val = node.val

        self._traverse(node.left)
        self._traverse(node.right)