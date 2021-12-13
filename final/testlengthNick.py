import unittest

from lengthNick import LengthNick

class TestLengthNick(unittest.TestCase):

    def setUp(self):
        self.m1 = LengthNick()

    def tearDown(self):
        pass

    def testdisplayNick(self):
        total = 0
        for i in self.m1.displayNick(3, ["None", "영어", "None", "None"], ["영어"]):
            total += i
        self.assertEqual(total, 3)
        total = 0
        for i in self.m1.displayNick(5, ["None", "영어", "숫자", "None"], ["영어", "숫자"]):
            total += i
        self.assertEqual(total, 5)
        total = 0
        for i in self.m1.displayNick(7, ["한글", "영어", "숫자", "None"], ["한글", "영어", "숫자"]):
            total += i
        self.assertEqual(total, 7)
        total = 0
        for i in self.m1.displayNick(11, ["한글", "영어", "숫자", "특수문자"], ["한글", "영어", "숫자", "특수문자"]):
            total += i
        self.assertEqual(total, 11)

if __name__ == '__main__':
    unittest.main()
