''' decorator to check if user exists and a funtion '''
import config
# import sys

# user = sys.argv[1]
# print(user)

# config.cursor.execute("SELECT * FROM users")
# users = config.cursor.fetchall()
def my_decorator(func):
    ''' decorator to check for user existence '''
    def wrapper(*args, **kwargs):
        ''' args[0] hae username and wrapper cheks if it exists or no '''
        # print(args)
        # print(config.users)

        config.cursor.execute(f"SELECT username FROM users WHERE username={args[0]}")
        users = config.cursor.fetchall()
        if bool(users):
            func(args[0])
        else:
            raise NameError
    return wrapper

@my_decorator
def my_func(user):
    ''' just checks decorator '''
    print(f"hello {user}!!")


# my_func = my_decorator(my_func('shaddygarg'))
# my_func('shaddygarg')
# my_func('rishi')

# cursor.close()
# cnx.close()
