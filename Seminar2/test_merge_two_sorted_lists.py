import unittest
from merge_two_sorted_lists import ListNode, Solution


class TestMergeTwoSortedLists(unittest.TestCase):
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

    def test_merge_two_lists_both_empty(self):
        list1 = self._create_linked_list([])
        list2 = self._create_linked_list([])
        solution = Solution()
        merged = solution.merge_two_lists(list1, list2)
        self.assertEqual(self._linked_list_to_list(merged), [])

    def test_merge_two_lists_one_empty(self):
        list1 = self._create_linked_list([1, 2, 4])
        list2 = self._create_linked_list([])
        solution = Solution()
        merged = solution.merge_two_lists(list1, list2)
        self.assertEqual(self._linked_list_to_list(merged), [1, 2, 4])

    def test_merge_two_lists_both_non_empty(self):
        list1 = self._create_linked_list([1, 3, 5])
        list2 = self._create_linked_list([2, 4, 6])
        solution = Solution()
        merged = solution.merge_two_lists(list1, list2)
        self.assertEqual(self._linked_list_to_list(merged), [1, 2, 3, 4, 5, 6])

    def test_merge_two_lists_different_lengths(self):
        list1 = self._create_linked_list([1, 3, 5, 7])
        list2 = self._create_linked_list([2, 4])
        solution = Solution()
        merged = solution.merge_two_lists(list1, list2)
        self.assertEqual(self._linked_list_to_list(merged), [1, 2, 3, 4, 5, 7])

    def test_merge_two_lists_single_element(self):
        list1 = self._create_linked_list([1])
        list2 = self._create_linked_list([2])
        solution = Solution()
        merged = solution.merge_two_lists(list1, list2)
        self.assertEqual(self._linked_list_to_list(merged), [1, 2])


if __name__ == "__main__":
    unittest.main()