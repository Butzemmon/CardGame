import card_factory

def compare_cards(card1, card2):

    for key in card_factory.values:
        if card_factory.values[key] == card1.value:
            value1 = key
        if card_factory.values[key] == card2.value:
            value2 = key

    if value1 > value2:
        return f'{card1.value} schlägt {card2.value}. Du gewinnst!'
    elif value2 > value1:
        return f'{card2.value} schlägt {card1.value}. Du verlierst!'
    else:
        for key in card_factory.suites:
            if card_factory.suites[key] == card1.suite:
                suite1 = key
            if card_factory.suites[key] == card2.suite:
                suite2 = key

        if suite1 > suite2:
            return f'{card1.suite} schlägt {card2.suite} bei gleichem Kartenwert. Du gewinnst!'
        elif suite2 > suite1:
            return f'{card2.suite} schlägt {card1.suite} bei gleichem Kartenwert. Du verlierst!'
        else:
            return "Unentschieden!"
