# IMPORT MODULES
import random

# CARD CLASS
class card:
    # suites -> h = heart   d = diamond
    #           s = spade   c = clover
    def __init__(self, suite: str, rank: int):
        # Check validity of arguments
        assert ((isinstance(suite, str)) and (suite == 'h' or suite == 'd' or suite == 's' or suite == 'c')), "suite is invalid"
        assert (isinstance(rank, int) and (rank > 0 and rank < 14)), "rank is invalid"

        # Pass arguments to object attributes
        self.suite = suite
        self.rank = rank

    def getrank(self):
        return self.rank

    def getsuite(self):
        return self.suite

    def __add__(card1, card2):
        return (card1.rank + card2.rank)

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
            print(f"{i}.) suite -> {self.set[i].suite}\trank -> {self.set[i].rank}")