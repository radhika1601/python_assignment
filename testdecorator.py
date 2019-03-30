import unittest
import checkuser
import io
import sys

class Testdecorator(unittest.TestCase):
	''' tests if decorator functions correctly '''
	def test_ExistingUser(self):
		''' for existing user functionality '''
		text = io.StringIO()
		sys.stdout = text

		checkuser.my_func('shaddygarg')

		sys.stdout = sys.__stdout__

		self.assertEqual(text.getvalue(), 'hello shaddygarg!!\n')

	def test_notExistingError(self):
		''' for non-existing users functionality '''
		self.assertRaises(NameError , checkuser.my_func, 'radhika')

if __name__ == '__main__':
    unittest.main()

