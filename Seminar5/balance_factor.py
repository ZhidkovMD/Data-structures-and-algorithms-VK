from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.balance_factor = 0


class Solution:
    def calculate_balance_factors(self, root: Optional[TreeNode]) -> None:
        self._compute_heights(root)

    def _compute_heights(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_height = self._compute_heights(node.left)
        right_height = self._compute_heights(node.right)

        node.balance_factor = left_height - right_height

        return max(left_height, right_height) + 1