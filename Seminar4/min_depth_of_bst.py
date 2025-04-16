from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.min_depth = float('inf')

        self._dfs(root, 0)

        return self.min_depth

    def _dfs(self, node: Optional[TreeNode], cur_depth: int) -> None:
        if not node:
            return

        if not node.left and not node.right:
            self.min_depth = min(self.min_depth, cur_depth + 1)

        self._dfs(node.left, cur_depth + 1)
        self._dfs(node.right, cur_depth + 1)