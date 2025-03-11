import unittest
from linked_list_cycle import ListNode, Solution


class TestSolution(unittest.TestCase):
    def test_has_cycle_no_cycle(self):
        #список без цикла: 1 -> 2 -> 3 -> 4
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)

        solution = Solution()
        self.assertFalse(solution.has_cycle(head))

    def test_has_cycle_with_cycle(self):
        #список с циклом: 1 -> 2 -> 3 -> 4 -> 2
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = head.next

        solution = Solution()
        self.assertTrue(solution.has_cycle(head))

    def test_has_cycle_single_node_no_cycle(self):
        #список из одного узла без цикла: 1
        head = ListNode(1)

        solution = Solution()
        self.assertFalse(solution.has_cycle(head))

    def test_has_cycle_single_node_with_cycle(self):
        #1 -> 1
        head = ListNode(1)
        head.next = head

        solution = Solution()
        self.assertTrue(solution.has_cycle(head))

    def test_has_cycle_empty_list(self):
        #пустой список
        head = None

        solution = Solution()
        self.assertFalse(solution.has_cycle(head))


if __name__ == "__main__":
    unittest.main()