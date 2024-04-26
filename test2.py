import unittest
from program2 import longest_substring

class TestLongestSubstring(unittest.TestCase):
    def test_longest_substring(self):
        self.assertEqual(longest_substring("abcabcbb"), 3)
        self.assertEqual(longest_substring("bbbbb"), 1)
        self.assertEqual(longest_substring("pwwkew"), 3)
        self.assertEqual(longest_substring("abcdefghijklmnopqrstuvwxyz"), 26)
        self.assertEqual(longest_substring("aab"), 2)
        self.assertEqual(longest_substring("dvdf"), 3)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



