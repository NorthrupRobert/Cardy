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
            if not (self.deck.set[i].rank > 10):
                sum += self.deck.set[i].rank
            elif self.deck.set[i].rank == 11:
                sum += 10
            elif self.deck.set[i].rank == 12:
                sum += 15
            elif self.deck.set[i].rank == 13:
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
        self.deck.shuffle()
        self.current_card = self.deck.draw()
        self.health = 20

    def attack(self):
        if self.current_card.rank == 11: # jack
            return 10
        elif self.current_card.rank == 12: # queen
            return 15
        return 20 # king

    def takedamage(self, damage: int):
        self.health -= damage

        if self.health < 0: # kill the enemy past max health
            return 1
        elif self.health == 0: # kill the enemy @ max health
            return 2
        else: # enemy survives
            return 0