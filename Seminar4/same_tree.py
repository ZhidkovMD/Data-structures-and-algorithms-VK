from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(
        self, 
        p: Optional[TreeNode], 
        q: Optional[TreeNode]
    ) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.is_same_tree(p.left, q.left) and 
                self.is_same_tree(p.right, q.right))