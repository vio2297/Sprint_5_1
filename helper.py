from random import randint


class Help:
    @staticmethod
    def generate_email():
        return f"test+{randint(0, 99999)}@mail.ru"