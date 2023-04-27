import random

class Player():
    def __init__(self, name, score=random.randint(1,100)):
        self.score = score
        self.name = name
        self.fantasyPoints = 0
        self.injured = False
