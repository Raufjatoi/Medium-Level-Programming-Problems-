# 5. Password Generator:
#  Create a program that generates a random password for the user.
#  The password should include a combination of uppercase and lowercase letters, numbers,
# and special characters.
#  Allow the user to specify the desired password length.
import random
import string
l = int(input('Enter the length of password '))
p = random.randint(string.ascii_uppercase,string.ascii_lowercase)
for i in range(l):
    print(p,end='')