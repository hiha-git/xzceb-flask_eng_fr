import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        with self.assertRaises(TypeError):
            english_to_french()  # Exception when required parameter not passed
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french(None), "")
        self.assertEqual(english_to_french(""), "")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        with self.assertRaises(TypeError):
            french_to_english()  # Exception when required parameter not passed
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english(None), "")
        self.assertEqual(french_to_english(""), "")

if "__main__" == __name__:
    unittest.main()
