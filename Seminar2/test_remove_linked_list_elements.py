import unittest
from remove_linked_list_elements import ListNode, Solution


class TestRemoveLinkedListElements(unittest.TestCase):
    def _create_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def _linked_list_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_remove_elements_no_removal(self):
        #1 -> 2 -> 3
        head = self._create_linked_list([1, 2, 3])
        solution = Solution()
        new_head = solution.remove_elements(head, 4)
        self.assertEqual(self._linked_list_to_list(new_head), [1, 2, 3])

    def test_remove_elements_all_elements(self):
        #2 -> 2 -> 2
        head = self._create_linked_list([2, 2, 2])
        solution = Solution()
        new_head = solution.remove_elements(head, 2)
        self.assertEqual(self._linked_list_to_list(new_head), [])

    def test_remove_elements_middle_elements(self):
        #1 -> 2 -> 3 -> 2 -> 4
        head = self._create_linked_list([1, 2, 3, 2, 4])
        solution = Solution()
        new_head = solution.remove_elements(head, 2)
        self.assertEqual(self._linked_list_to_list(new_head), [1, 3, 4])

    def test_remove_elements_head_elements(self):
        #1 -> 1 -> 2 -> 3
        head = self._create_linked_list([1, 1, 2, 3])
        solution = Solution()
        new_head = solution.remove_elements(head, 1)
        self.assertEqual(self._linked_list_to_list(new_head), [2, 3])

    def test_remove_elements_tail_elements(self):
        # 1 -> 2 -> 3 -> 3
        head = self._create_linked_list([1, 2, 3, 3])
        solution = Solution()
        new_head = solution.remove_elements(head, 3)
        self.assertEqual(self._linked_list_to_list(new_head), [1, 2])

    def test_remove_elements_empty_list(self):
        #пустой список
        head = self._create_linked_list([])
        solution = Solution()
        new_head = solution.remove_elements(head, 1)
        self.assertEqual(self._linked_list_to_list(new_head), [])


if __name__ == "__main__":
    unittest.main()