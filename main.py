import generator
import card_combat
def main():

    card1 = generator.generate_card()
    card1.show_card()
    card2 = generator.generate_card()
    card2.show_card()
    print(card_combat.compare_cards(card1, card2))

if __name__ == '__main__':
    main()
