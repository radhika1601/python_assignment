''' scrap function to scrape data '''

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
        print and store name and city
    '''
    query1 = f"SELECT scrape,name,city FROM users WHERE username = \"{username}\""
    config.cursor.execute(query1)
    credentials = config.cursor.fetchall()[0]
    scrape = credentials[0]

    if scrape == 0:
        fb_url = "https://en-gb.facebook.com/{}".format(username)
        # print(fb)
        page = urllib.request.urlopen(fb_url)
        soup = BeautifulSoup(page, features="html.parser")

        for uname in soup.find_all('a', class_='_2nlw _2nlv'):
            name = uname.text.strip()

        city = []
        for cityname in soup.find_all('span', class_='_2iel _50f7'):
            city.append(cityname.text.strip())

        current_city = city[0]

        works = []
        for work in soup.find_all('div', class_='_2lzr _50f5 _50f7'):
            works.append(work.text.strip())

        keys = []
        for key in soup.find_all('div', class_='labelContainer'):
            keys.append(key.text.strip())

        if bool(keys):
            fav = {}
            i = 0
            for value in soup.find_all('div', class_='mediaPageName'):
                fav[keys[i]] = value.text.strip()
                i = i+1
        else:
            fav = "There are no favourites"

        if bool(current_city):
            person1 = person.Person(name, current_city, works)
        else:
            person1 = person.Person(name, None, works)
        # print(works)
        print(fav)
        query = f"UPDATE users SET scrape=1,name=\'{person1.name}\',city=\'{person1.city}\' WHERE username=\'{username}\'"
        config.cursor.execute(query)
        config.cnx.commit()
        # print(query)
        # print("Info Updated")

    else:
        person1 = person.Person(credentials[1], credentials[2])
        person1.show()

# scrap("swapnil.negi09")
