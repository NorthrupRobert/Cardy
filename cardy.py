# IMPORT MODULES
import random

# CARD CLASS
class card:
    # suites -> 1 = heart   2 = diamond
    #           3 = spade   4 = clover
    def __init__(self, suite: int, value):
        # Check validity of arguments
        assert ((isinstance(suite, int)) and (suite > 0 and suite < 5)), "suite is invalid"
        assert (isinstance(value, int) and (value > 0 and value < 14)), "value is invalid"

        # Pass arguments to object attributes
        self.suite = suite
        self.value = value

    def getvalue(self):
        return self.value

    def getsuite(self):
        return self.suite

    def __add__(card1, card2):
        return (card1.value + card2.value)

# DECK CLASS
class deck:
    # constructor w/ preset deck
    def __init__(self, cards: list = []):
        # Check validity of arguments
        assert (isinstance(cards, list) or isinstance(cards, tuple)), "deck parameter is not an iterable"

        # Pass arguments
        if isinstance(cards, list):
            self.set = cards
        else:
            self.set = list(cards)
        self.numcards = int(len(self.set))

    def shuffle(self):
        random.seed()
        random.shuffle(self.set)

    def addbottom(self, new_card):
        assert isinstance(new_card, card), "appending instance not of card type to set"
        self.set.insert(0, new_card) # index, element

    def addtop(self, new_card):
        assert isinstance(new_card, card), "appending instance not of card type to set"
        self.set.append(new_card)

    def draw(self):
        send_card = self.set[len(self.set) - 1]
        self.set.pop()
        return send_card
    
    def drawindex(self, index):
        send_card = self.set[index]
        for i in range(index, len(self.set) - 1):
            self.set[i] = self.set[i + 1]
        self.set.pop()
        return send_card

    def findcardindex(self, card):
        return self.set.index(card)

    def getnumcards(self):
        return self.numcards

    def printdeck(self):
        for i in range(len(self.set)):
            print(f"{i}.) suite -> {self.set[i].suite}\tvalue -> {self.set[i].value}")