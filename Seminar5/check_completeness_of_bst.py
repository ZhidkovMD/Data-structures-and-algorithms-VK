from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_complete_tree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        found_null = False

        while queue:
            node = queue.popleft()

            if not node:
                found_null = True
            else:
                if found_null:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True