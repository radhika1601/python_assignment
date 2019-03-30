import config 
import sys

# user = sys.argv[1]
# print(user)

config.cursor.execute("SELECT * FROM users")
users = config.cursor.fetchall()
def my_decorator(func):
	def wrapper(*args, **kwargs):
		# print(args)
		# print(config.users)
		if any(args[0] in username for username in users):
				func(args[0])
		else:
			exceptionName()
	return wrapper

@my_decorator
def my_func(user):
	print(f"hello {user}!!")

def exceptionName():
	raise NameError



# my_func = my_decorator(my_func('shaddygarg'))
# my_func('shaddygarg')
# my_func('rishi')

# cursor.close()
# cnx.close()