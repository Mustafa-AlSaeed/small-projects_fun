import random
import string

characters = list (string.ascii_letters + string.digits + "!@#$%^&*()")

def rando_password():
    user_request = int(input("Length of password required"))

    #shuffling the cvharacter
    random.shuffle(characters)

    #I need to mak3e an empty list to store my generated password in
    password = []

    for i in range(user_request):
        password.append(random.choice(characters))

    random.shuffle(password)

    print(''.join(password))

rando_password()

    
