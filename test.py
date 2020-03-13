import unittest

def booksearch():
    return {}

class BookSearchTest(unittest.TestCase):
    def test_booksearch(self):
        self.assertEqual({}, booksearch())

