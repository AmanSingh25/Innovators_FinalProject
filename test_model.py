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
        self.assertEquals(is_valid_password("aBc1234!"), False)








