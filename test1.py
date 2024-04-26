import unittest
from program1 import smallest_missing_positive_integer

class TestSmallestMissingPositiveInteger(unittest.TestCase):
    def test_smallest_missing_positive_integer(self):
        self.assertEqual(smallest_missing_positive_integer([3, 4, -1, 1]), 2)
        self.assertEqual(smallest_missing_positive_integer([1, 2, 0]), 3)
        self.assertEqual(smallest_missing_positive_integer([-1, -3, 4, 2]), 1)
        self.assertEqual(smallest_missing_positive_integer([1, 2, 3]), 4)
        self.assertEqual(smallest_missing_positive_integer([-1, -2, -3]), 1)
        self.assertEqual(smallest_missing_positive_integer([1, 2, 3, 4, 5, 6, 7, 8, 9]), 10)
        self.assertEqual(smallest_missing_positive_integer([]), 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



