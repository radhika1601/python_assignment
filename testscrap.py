''' tests for scrap.py '''
import unittest
import io
import sys
from scrap import scrap
import config

class TestScrap(unittest.TestCase):
    ''' tests functionality of scrap funtion '''
    def test1(self):
        '''' should raise name error for non-existent username in db '''
        self.assertRaises(NameError, scrap, 'radhika')

    username = 'k4ni5h'
    def setUp(self):
        query = f"UPDATE users SET scrape=0,name=NULL,city=NULL WHERE username=\'{self.username}\'"
        config.cursor.execute(query)
        config.cnx.commit()

    def test2(self):
        ''' checks if data is scraped correctly for existing user with unscrapped data '''
        scrap(self.username)
        config.cursor.execute(f"SELECT scrape,name,city FROM users WHERE username=\"{self.username}\"")
        self.credentials = config.cursor.fetchall()[0]
        self.assertEqual(1, self.credentials[0])

    def test3(self):
        ''' checks if it just renders previous data if the data for respective user is already scraped '''
        scrap(self.username)
        text2 = io.StringIO()
        sys.stdout = text2
        scrap(self.username)
        sys.stdout = sys.__stdout__

        self.assertEqual(text2.getvalue(), 'My name is Kanish and my current city is Roorkee\n')

    def test4(self):
        ''' checks functionality if there are no favourites '''
        query = f"UPDATE users SET scrape=0,name=NULL,city=NULL WHERE username=\'{'swapnil.negi09'}\'"
        config.cursor.execute(query)
        config.cnx.commit()
        text3 = io.StringIO()
        sys.stdout = text3
        scrap('swapnil.negi09')
        self.assertEqual(text3.getvalue(), "There are no favourites\n")

    def tearDown(self):
        query = f"UPDATE users SET scrape=0,name=NULL,city=NULL WHERE username=\'{self.username}\'"
        config.cursor.execute(query)
        config.cnx.commit()

if __name__ == '__main__':
    unittest.main()
