
class Registration:
    def __init__(self, login):
        self.login = login

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if "@" in value:
            if value.count(".", value.find("@")) == 1:
                self.__login = value
            else:
                raise ValueError("Логин должен содержать символ '.'")
        else:
            raise ValueError("Логин должен содержать один символ '@'")


r1 = Registration('qwerty@rambler.ru') # здесь хороший логин
print(r1.login)