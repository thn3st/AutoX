import random
import string


class StringRandomHelper:
    @staticmethod
    def generate_string(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y)).lower()

    @staticmethod
    def generate_password(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))

