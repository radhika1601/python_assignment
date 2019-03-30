import urllib.request
from bs4 import BeautifulSoup
import config
import person
from checkuser import my_decorator

@my_decorator
def scrap(username):
    '''
        scrapes data from facebook for the available user in db
        print favourites
        print name and city
    '''
    config.cursor.execute("SELECT scrape,name,city FROM users WHERE username = \"{}\"".format(username))
    credentials = config.cursor.fetchall()[0]
    scrape = credentials[0]

    if scrape == 0:
    	fb = "https://en-gb.facebook.com/{}".format(username)
    	# print(fb)
    	page = urllib.request.urlopen(fb)
    	soup = BeautifulSoup(page, features="html.parser")

    	for u in soup.find_all('a', class_='_2nlw _2nlv'):
    		name = u.text.strip()

    	city = []
    	for c in soup.find_all('span', class_='_2iel _50f7'):
    		city.append(c.text.strip())

    	current_city = city[0]

    	works = []
    	for w in soup.find_all('div', class_='_2lzr _50f5 _50f7'):
    		works.append(w.text.strip())

        keys = []
        for k in soup.find_all('div', class_='labelContainer'):
    		keys.append(k.text.strip())

        if bool(keys):
    		fav = {}
    		i = 0
    		for v in soup.find_all('div', class_='mediaPageName'):
    			fav[keys[i]] = v.text.strip()
    			i = i+1
    	else:
    		fav = "There are no favourites"

    	if bool(current_city):
    		p = person.Person(name, current_city, works)
    	else:
    		p = person.Person(name,None,works)
    	# print(works)
    	print(fav)
    	query = f"UPDATE users SET scrape = 1, name =  \'{p.name}\',city=\'{p.city}\' WHERE username = \'{username}\'"
    	config.cursor.execute(query)
    	config.cnx.commit()
    	# print(query)
    	# print("Info Updated")

    else:
    	p = person.Person(credentials[1], credentials[2])
    	p.show()

# scrap("swapnil.negi09")