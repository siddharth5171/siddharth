# write a program to check entered username and password is correect 
# or not tale username and password from user and compare it with correct 
# username and password. prepare two exeptions classes  for username and one for password.  raise 
# exception object according to the condition.





class UsernameException(Exception):
    pass

class PasswordException(Exception):
    pass

correct_username = "siddharth"
correct_password = "siddharth123"

try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != correct_username:
        raise UsernameException("Invalid username!")

    if password != correct_password:
        raise PasswordException("Invalid password!")

    print("Login successful!")

except UsernameException as e:
    print(e)

except PasswordException as e:
    print(e)
