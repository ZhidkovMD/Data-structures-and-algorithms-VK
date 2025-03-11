import unittest
from reverse_linked_list import ListNode, IterativeSolution, RecursiveSolution


class TestReverseLinkedList(unittest.TestCase):
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

    def _test_reverse(self, solution):
        #пустой список
        self.assertIsNone(solution.reverse_list(None))

        #список из одного элемента
        head = self._create_linked_list([1])
        reversed_head = solution.reverse_list(head)
        self.assertEqual(self._linked_list_to_list(reversed_head), [1])

        #список из нескольких элементов
        head = self._create_linked_list([1, 2, 3, 4, 5])
        reversed_head = solution.reverse_list(head)
        self.assertEqual(self._linked_list_to_list(reversed_head), [5, 4, 3, 2, 1])

        #список из нескольких элементов
        head = self._create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
        reversed_head = solution.reverse_list(head)
        self.assertEqual(self._linked_list_to_list(reversed_head), [8, 7, 6, 5, 4, 3, 2, 1])

        #список с двумя элементами
        head = self._create_linked_list([1, 2])
        reversed_head = solution.reverse_list(head)
        self.assertEqual(self._linked_list_to_list(reversed_head), [2, 1])

    def test_iterative_solution(self):
        solution = IterativeSolution()
        self._test_reverse(solution)

    def test_recursive_solution(self):
        solution = RecursiveSolution()
        self._test_reverse(solution)


if __name__ == "__main__":
    unittest.main()