from model import *
import unittest

class TestModel(unittest.TestCase):

    def test_if_empty(self):
        self.assertEquals(is_all_empty(""), True)
        self.assertEquals(is_all_empty("random"), False)
        self.assertEquals(is_all_empty("90232"), False)
        self.assertEquals(is_all_empty("  "), False)

    def test_valid_password(self):
        #invalid type
        self.assertRaises(TypeError, is_valid_password, 101)
        self.assertRaises(TypeError, is_valid_password, -1.01)

        #invalid password length
        self.assertRaises(ValueError, is_valid_password, "abcd")
        self.assertRaises(ValueError, is_valid_password, "")

        #for all special char, lower case and upper cases and a num 
        self.assertEquals(is_valid_password("Abc1@"), True)
        self.assertEquals(is_valid_password("bcd123"), False)
        self.assertEquals(is_valid_password("@@@12"), False)
        self.assertEquals(is_valid_password("aBc1234!"), True)
    
    def test_is_url_valid(self):
        #jpg
        self.assertEquals(is_valid_url("https://upload.wikimedia.org/wikipedia/commons/4/47/New_york_times_square-terabass.jpg"), True)
        #jpeg
        self.assertEquals(is_valid_url("data:image/jpeg;base64,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"), True)
        #.com
        self.assertEquals(is_valid_url("www.instagram.com"), False)
