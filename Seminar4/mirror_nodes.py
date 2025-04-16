from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def count_mirror_nodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        count = 0
        stack = [(root.left, root.right)]
        
        while stack:
            left, right = stack.pop()
            
            if left and right and left.val == right.val:
                count += 2
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
        
        return count