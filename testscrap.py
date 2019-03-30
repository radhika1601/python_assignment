from scrap import scrap
import config
import unittest
import io
import sys

class Test_scrap(unittest.TestCase):

	def testFornonExistingUser(self):
		self.assertRaises(NameError , scrap, 'radhika')
	
	username = 'k4ni5h'
	def setUp(self):
		query = "UPDATE users SET scrape = 0, name=NULL, city=NULL WHERE username = \'{}\'".format(self.username)
		config.cursor.execute(query)
		config.cnx.commit()

	def testForExistingUserUnscrapedData(self):
		scrap(self.username)
		config.cursor.execute("SELECT scrape,name,city FROM users WHERE username = \"{}\"".format(self.username))
		self.credentials = config.cursor.fetchall()[0]
		self.assertEqual(1, self.credentials[0])

	def testForExistingUserScrappedData(self):
		scrap(self.username)
		text2 = io.StringIO()
		sys.stdout = text2

		scrap(self.username)
		sys.stdout = sys.__stdout__

		self.assertEqual(text2.getvalue(), 'My name is Kanish and my current city is Roorkee\n')


	# def testCheckIfNoWork(self):
	# 	try:
	# 		hasattr(scrap('k4ni5h'), 'works');
	# 	except:
	# 		pass


	# 	# self.assertEqual(fav, "There are no favourites")



	def tearDown(self):
		query = "UPDATE users SET scrape = 0, name =  NULL,city=NULL WHERE username = \'{}\'".format(self.username)
		config.cursor.execute(query)
		config.cnx.commit()

if __name__ == '__main__':
    unittest.main()