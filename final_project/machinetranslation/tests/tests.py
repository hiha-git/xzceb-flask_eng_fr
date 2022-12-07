import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french_exception(self):
        with self.assertRaises(TypeError):
            english_to_french()  # Exception when required parameter not passed
    def test_english_to_french_assertEqual_string(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_english_to_french_assertEqual_None(self):
        self.assertEqual(english_to_french(None), "")
    def test_english_to_french_assertEqual_empty_string(self):
        self.assertEqual(english_to_french(""), "")
    def test_english_to_french_assertNotEqual(self):
        self.assertNotEqual(english_to_french('None'), '   ')  # from discussion board

class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english_exception(self):
        with self.assertRaises(TypeError):
            french_to_english()  # Exception when required parameter not passed
    def test_french_to_english_assertEqual_string(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test_french_to_english_assertEqual_None(self):
        self.assertEqual(french_to_english(None), "")
    def test_french_to_english_assertEqual_empty_string(self):
        self.assertEqual(french_to_english(""), "")
    def test_french_to_english_assertNotEqual(self):
        self.assertNotEqual(french_to_english('None'), '   ')  # from discussion board

if "__main__" == __name__:
    unittest.main()
