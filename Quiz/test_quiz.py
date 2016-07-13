import unittest
import quiz

class Problem4Test(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertFalse(quiz.isPalindrome('tacovgcat'))
    def test_isPalindrome2(self):
        self.assertTrue(quiz.isPalindrome('tacocat'))

class Problem5Test(unittest.TestCase):
	def testDotProduct(self):
		self.assertEqual(quiz.dotProduct([1,2,3],[4,5,6]), 32)


class Problem6Test(unittest.TestCase):
	def testFlatten(self):
		self.assertEqual(quiz.flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]), [1,'a','cat',2,3,'dog',4,5])


class Problem7Test(unittest.TestCase):
    def test_dict_interdiff(self):
        d1 = {1:30, 2:20, 3:30, 5:80}
        d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
        self.assertEqual(quiz.dict_interdiff(d1, d2), ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90}))
    def test_dict_interdiff2(self):
        d1 = {1:30, 2:20, 3:30}
        d2 = {1:40, 2:50, 3:60}
        self.assertEqual(quiz.dict_interdiff(d1, d2), ({1: False, 2: False, 3: False}, {}))


unittest.main()
