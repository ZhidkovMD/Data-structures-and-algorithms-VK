from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_subtree(
        self,
        root: Optional[TreeNode],
        sub_root: Optional[TreeNode]
    ) -> bool:
        if not sub_root:
            return True
        if not root:
            return False
        if self._same_tree(root, sub_root):
            return True

        return (self.is_subtree(root.left, sub_root) or
                self.is_subtree(root.right, sub_root))

    def _same_tree(
        self,
        root: Optional[TreeNode],
        sub_root: Optional[TreeNode]
    ) -> bool:
        if not root and not sub_root:
            return True
        if root and sub_root and root.val == sub_root.val:
            return (self._same_tree(root.left, sub_root.left)) and \
                   (self._same_tree(root.right, sub_root.right))
        return False