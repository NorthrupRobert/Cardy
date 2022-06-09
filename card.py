# Class definition of card, contains values like suite, value, etc.
class card:
    def __init__(self, suite, value):
        print("\tCARD CONSTRUCTOR")
        
        self.suite = suite
        self.value = value