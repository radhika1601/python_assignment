from person import Person
import unittest
import io
import sys

class TestPerson(unittest.TestCase):

	p1 = Person('radhika', 'balotra', ['student',])

	def test_personWithAllParam_show(self):
		text = io.StringIO()
		sys.stdout = text

		self.p1.show()
		sys.stdout = sys.__stdout__

		self.assertEqual(text.getvalue(), 'My name is radhika and my current city is balotra\n')

	def test_personWithAllParam_work(self):
		self.assertEqual(self.p1.work, ['student'])

	p2 = Person('radhika', 'balotra')

	def test_PersonwithnoWorkParam(self):
		try:
			self.p2.work
		except AttributeError:
			pass

	p3 = Person('radhika')
	def test_personwithonlynameparam(self):
		text = io.StringIO()
		sys.stdout = text

		self.p3.show()
		sys.stdout = sys.__stdout__
		self.assertEqual(text.getvalue(), 'My name is radhika and my current city is Roorkee\n')

if __name__ == '__main__':
    unittest.main()
