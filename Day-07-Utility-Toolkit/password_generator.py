import random
import string

def password_generator(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(all_characters, k=length))

    return password