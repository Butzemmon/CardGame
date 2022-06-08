class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def show_card(self):
        print(self.suite, self.value)
