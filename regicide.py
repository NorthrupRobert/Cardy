import cardy

# PLAYER CLASS
class player:
    def __init__(self, max_hand_size: int, new_deck = cardy.deck()):
        assert isinstance(max_hand_size, int), "hand size must be of type int"
        assert isinstance(new_deck, cardy.deck), "an argument of type cardy.deck must be passed to the player constructor"
        assert (max_hand_size + 1) > new_deck.getnumcards(), "hand size cannot compensate for the number of cards when constructing player"

        self.deck = new_deck
        self.updatehealth()

    def updatehealth(self):
        sum = 0
        for i in range(len(self.deck.set)):
            if not (self.deck.set[i].value > 10):
                sum += self.deck.set[i].value
            elif self.deck.set[i].value == 11:
                sum += 10
            elif self.deck.set[i].value == 12:
                sum += 15
            elif self.deck.set[i].value == 13:
                sum += 20
            else:
                raise Exception("invalid card: regicide/player/updatehealth")
        self.health = sum
        return sum

    def add(self, new_card):
        self.deck.addtop(new_card)
        return True

    def remove(self, remove_card):
        return self.deck.drawindex(self.deck.findcardindex)
        

class enemy:
    def __init__(self, new_deck):
        assert isinstance(new_deck, cardy.deck), "an argument of type cardy.deck must be passed to the player constructor"

        self.deck = new_deck
