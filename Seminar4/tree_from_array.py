from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def array_to_tree(self, nums: List[Optional[int]]) -> Optional[TreeNode]:
        if not nums or nums[0] is None:
            return None

        root = TreeNode(nums[0])
        queue = [root]
        i = 1

        while queue and i < len(nums):
            current = queue.pop(0)

            if i < len(nums) and nums[i] is not None:
                current.left = TreeNode(nums[i])
                queue.append(current.left)
            i += 1

            if i < len(nums) and nums[i] is not None:
                current.right = TreeNode(nums[i])
                queue.append(current.right)
            i += 1

        return root