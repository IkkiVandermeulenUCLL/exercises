from util import *
def count_older_than(people, min_age):
    def is_older(x):
        return x.age>= min_age
    return count(people, is_older)

def indices_of_cards_with_suit(cards, suit):
    result =[]
    def equal_suit(x):
        return x.suit==suit
    return indices_of(cards, equal_suit)