import card
import card_factory
import random

def generate_card():
    new_card = card.Card(card_factory.suites[random.randint(1,4)], card_factory.values[random.randint(2,14)])
    return new_card
