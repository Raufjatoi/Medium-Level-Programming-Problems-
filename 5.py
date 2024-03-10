# 5. Password Generator:
#  Create a program that generates a random password for the user.
#  The password should include a combination of uppercase and lowercase letters, numbers,
# and special characters.
#  Allow the user to specify the desired password length.

import random
import string

length = int(input('Enter the length of the password: '))

password = ''
for _ in range(length):
    password += random.choice(string.ascii_letters + string.digits + string.punctuation)

print('Generated Password:', password)
