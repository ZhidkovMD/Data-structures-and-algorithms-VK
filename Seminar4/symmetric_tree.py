from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        def _dfs(left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:
            if not left_node and not right_node:
                return True
            if not left_node or not right_node:
                return False
            return (left_node.val == right_node.val and
                    _dfs(left_node.left, right_node.right) and
                    _dfs(left_node.right, right_node.left))

        if not root:
            return True
        return _dfs(root.left, root.right)