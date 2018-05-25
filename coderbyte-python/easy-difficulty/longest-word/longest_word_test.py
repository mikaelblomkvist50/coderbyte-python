import unittest

import longest_word

class LongestWordTests(unittest.TestCase):
    def test_longest_word(self):
        self.assertEqual(longet_word.longest_word("The quick brown fox jumped over the lazy dog"), 'jumped')
