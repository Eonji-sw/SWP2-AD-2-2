import unittest

from wordNick import WordNick

class TestWordNick(unittest.TestCase):

    def setUp(self):
        self.w1 = WordNick()

    def tearDown(self):
        pass

    def testrandFun(self):
        self.w1.randFun([0, 5, 2, 0])
        self.assertEqual(len(self.w1.finalNick), 7)
        self.w1.finalNick = ''
        self.w1.randFun([0, 0, 2, 8])
        self.assertEqual(len(self.w1.finalNick), 10)
        self.w1.finalNick = ''
        self.w1.randFun([4, 5, 2, 3])
        self.assertEqual(len(self.w1.finalNick), 14)

if __name__ == '__main__':
    unittest.main()
