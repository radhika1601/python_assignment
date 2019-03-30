'''tests for person.py '''
import unittest
import io
import sys
from person import Person

class TestPerson(unittest.TestCase):
    '''tests for person  '''
    person1 = Person('radhika', 'balotra', ['student',])

    def testshow(self):
        ''' checks output when person is initialised with all params '''
        text = io.StringIO()
        sys.stdout = text

        self.person1.show()
        sys.stdout = sys.__stdout__

        self.assertEqual(text.getvalue(), 'My name is radhika and my current city is balotra\n')

    def testwork(self):
        ''' checks if work param takes expected value when passed'''
        self.assertEqual(self.person1.work, ['student'])

    person2 = Person('radhika')

    def testnoWork(self):
        ''' if no work param passed checks for it not being initialised '''
        try:
            self.person2.work
        except AttributeError:
            pass

    def testnocity(self):
        ''' checks if city takes its default when value when no param other than name is passed '''
        text = io.StringIO()
        sys.stdout = text

        self.person2.show()
        sys.stdout = sys.__stdout__
        self.assertEqual(text.getvalue(), 'My name is radhika and my current city is Roorkee\n')

if __name__ == '__main__':
    unittest.main()
