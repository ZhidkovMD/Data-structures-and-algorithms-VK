import unittest
from anagrams import group_anagrams


class TestGroupAnagrams(unittest.TestCase):
    def test_basic_case(self):
        input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        result = group_anagrams(input_strs)
        self.assertEqual(len(result), len(expected))
        for group in expected:
            self.assertIn(sorted(group), [sorted(r) for r in result])

    def test_empty_input(self):
        self.assertEqual(group_anagrams([]), [])

    def test_single_word(self):
        self.assertEqual(group_anagrams(["a"]), [["a"]])

    def test_multiple_groups(self):
        input_strs = ["abc", "cba", "bac", "xyz", "zyx"]
        expected = [["abc", "cba", "bac"], ["xyz", "zyx"]]
        result = group_anagrams(input_strs)
        for group in expected:
            self.assertIn(sorted(group), [sorted(r) for r in result])

    def test_case_sensitivity(self):
        input_strs = ["stop", "pots", "tops", "opts"]
        expected = [["stop", "pots", "tops", "opts"]]
        result = group_anagrams(input_strs)
        self.assertEqual(len(result), len(expected))
        self.assertEqual(sorted(result[0]), sorted(expected[0]))


if __name__ == '__main__':
    unittest.main()