from random import shuffle


class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, value) -> None:
        if suit not in Card.suits and value not in Card.values:
            raise ValueError("Not valid suit or card")
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        return f"{self.value} of {self.suit} "
        # return "{} of {}".format(self.value, self.suit)


class Deck:
    from random import shuffle

    def __init__(self) -> None:
        self.cards = [Card(suit, value)
                      for suit in Card.suits for value in Card.values]
        self.newlist = []

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

    def _deal(self, number=1):
        if number > self.count():
            raise ValueError("All cards have been dealt")
        self.newlist = self.cards[-number::]
        self.cards = self.cards[:-number:]
        return self.newlist

    def deal_card(self):
        return self._deal()

    def deal_hand(self, number):
        return self._deal(number)

    def __repr__(self) -> str:
        return f"Deck of {self.count()} cards "
        # return "Deck of {}".format(self.count())


d1 = Deck()
d1.shuffle()
# print(d1.cards)
# d1.deal_card()
# print(d1)
x = d1.deal_hand(5)
print(d1)
print(x)
d1.deal_hand(4)
print(d1)
d1.deal_hand(3)
print(d1)
d1.deal_hand(5)
print(d1)
d1.deal_hand(20)
print(d1)
d1.deal_hand(14)
print(d1)
d1.deal_card()
print(d1)
