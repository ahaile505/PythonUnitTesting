
class PhoneBook:

    def __init__(self) -> None:
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers.get(name)
    
    def names(self):
        return set(self.numbers.keys())