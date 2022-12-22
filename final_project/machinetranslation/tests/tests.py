import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(None), '') # test None input
        self.assertEqual(english_to_french(''), '') # test empty input
    def test2(self):    
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test Hello -> Bonjour
        self.assertNotEqual(english_to_french('Morning'), 'Morning') # test Morning

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(None), '') # test None input
        self.assertEqual(french_to_english(''), '') # test empty input
    def test2(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test Bonjour -> Hello
        self.assertNotEqual(french_to_english('Vie'), 'Live') # test Morning

        
unittest.main()
