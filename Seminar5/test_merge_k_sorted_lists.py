import unittest
from merge_k_sorted_lists import ListNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertIsNone(self.solution.merge_k_lists([]))

    def test_single_list(self):
        l1 = ListNode(1, ListNode(2, ListNode(3)))
        result = self.solution.merge_k_lists([l1])
        self._verify_list(result, [1, 2, 3])

    def test_two_lists(self):
        l1 = ListNode(1, ListNode(4, ListNode(5)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        result = self.solution.merge_k_lists([l1, l2])
        self._verify_list(result, [1, 1, 3, 4, 4, 5])

    def test_three_lists(self):
        l1 = ListNode(1, ListNode(4, ListNode(5)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        l3 = ListNode(2, ListNode(6))
        result = self.solution.merge_k_lists([l1, l2, l3])
        self._verify_list(result, [1, 1, 2, 3, 4, 4, 5, 6])

    def test_with_empty_lists(self):
        l1 = ListNode(1, ListNode(2))
        l2 = None
        l3 = ListNode(3, ListNode(4))
        result = self.solution.merge_k_lists([l1, l2, l3])
        self._verify_list(result, [1, 2, 3, 4])

    def test_all_empty_lists(self):
        self.assertIsNone(self.solution.merge_k_lists([None, None]))

    def _verify_list(self, head: ListNode, expected: list):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        self.assertEqual(values, expected)


if __name__ == '__main__':
    unittest.main()