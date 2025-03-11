from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class IterativeSolution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


class RecursiveSolution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverse_list(head.next)
            head.next.next = head
        head.next = None

        return new_head