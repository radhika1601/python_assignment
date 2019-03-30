''' defines object person '''

class Person(): # pylint: disable=too-few-public-methods
    '''
    has name(compulsory), city, work if any
    '''
    def __init__(self, name, city="Roorkee", *args):
        ''' constructor '''
        self.name = name
        self.city = city
        if bool(args):
            self.work = args[0]

    def show(self):
        ''' function to display info '''
        print(f"My name is {self.name} and my current city is {self.city}")


# p1 = Person("radhika", "balotra","student")
# p1.show()
# print(p1.work)
# p2 = Person('surya')
# p2.show()
# print(p2.work)
