import unittest
from middle_of_linked_list import ListNode, Solution


class TestMiddleOfLinkedList(unittest.TestCase):
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

    def test_middle_node_odd_length(self):
        #1 -> 2 -> 3 -> 4 -> 5
        head = self._create_linked_list([1, 2, 3, 4, 5])
        solution = Solution()
        middle_node = solution.middle_node(head)
        self.assertEqual(self._linked_list_to_list(middle_node), [3, 4, 5])

    def test_middle_node_even_length(self):
        #1 -> 2 -> 3 -> 4 -> 5 -> 6
        head = self._create_linked_list([1, 2, 3, 4, 5, 6])
        solution = Solution()
        middle_node = solution.middle_node(head)
        self.assertEqual(self._linked_list_to_list(middle_node), [4, 5, 6])

    def test_middle_node_single_element(self):
        #1
        head = self._create_linked_list([1])
        solution = Solution()
        middle_node = solution.middle_node(head)
        self.assertEqual(self._linked_list_to_list(middle_node), [1])

    def test_middle_node_empty_list(self):
        #пустой список
        head = self._create_linked_list([])
        solution = Solution()
        middle_node = solution.middle_node(head)
        self.assertIsNone(middle_node)


if __name__ == "__main__":
    unittest.main()