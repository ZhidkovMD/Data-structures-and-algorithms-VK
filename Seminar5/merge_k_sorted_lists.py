from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_k_lists(
        self, 
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            new_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                new_lists.append(self._merge_two_lists(l1, l2))
            lists = new_lists

        return lists[0]

    def _merge_two_lists(
        self, 
        l1: Optional[ListNode], 
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next