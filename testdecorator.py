import unittest
import checkuser
import io
import sys

class Testdecorator(unittest.TestCase):

	def test_ExistingUser(self):
		text = io.StringIO()
		sys.stdout = text

		checkuser.my_func('shaddygarg')

		sys.stdout = sys.__stdout__

		self.assertEqual(text.getvalue(), 'hello shaddygarg!!\n')

	def test_notExistingError(self):
		self.assertRaises(NameError , checkuser.my_func, 'radhika')

if __name__ == '__main__':
    unittest.main()

