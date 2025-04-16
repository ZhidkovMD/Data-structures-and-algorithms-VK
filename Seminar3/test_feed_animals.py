import unittest
from feed_animals import max_fed_animals


class TestMaxFedAnimals(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(max_fed_animals([1, 2, 3], [3, 2, 1]), 3)

    def test_unequal_amounts(self):
        self.assertEqual(max_fed_animals([1, 1, 1], [1, 1]), 2)

    def test_large_animals(self):
        self.assertEqual(max_fed_animals([4, 8, 3], [8, 3, 4]), 3)

    def test_not_enough_food(self):
        self.assertEqual(max_fed_animals([5, 6, 7], [4, 3]), 0)

    def test_mixed_case(self):
        self.assertEqual(max_fed_animals([2, 3, 4, 5], [5, 4, 3, 2]), 4)

    def test_single_animal(self):
        self.assertEqual(max_fed_animals([8], [8]), 1)

    def test_empty_input(self):
        self.assertEqual(max_fed_animals([], [5, 3]), 0)
        self.assertEqual(max_fed_animals([3, 2], []), 0)

    def test_performance_large_input(self):
        animals = [i % 10 + 1 for i in range(100000)]
        food = [i % 10 + 1 for i in range(100000)]
        self.assertEqual(max_fed_animals(animals, food), 100000)


if __name__ == '__main__':
    unittest.main()