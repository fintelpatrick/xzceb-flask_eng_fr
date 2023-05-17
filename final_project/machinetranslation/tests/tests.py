"""Tests for the translator module"""

import unittest
from translator import english_to_french
from translator import french_to_english

class TestEnglishToFre(unittest.TestCase):
    """Test the english to french translator"""
    def test1(self):
        """Test null and 'Hello'"""
        self.assertEqual(english_to_french(' '), ' ')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEng(unittest.TestCase):
    """Test the french to english translator"""
    def test1(self):
        """Test null and 'Bonjour'"""
        self.assertEqual(french_to_english(' '), ' ')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()

print(english_to_french('Hello'))
