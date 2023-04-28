import random
import math
from settings import *
import player

class Team():
    def __init__(self, name, goodness=random.randint(1, 100)):
        self.name = name
        self.goodness = goodness
        self.players = []
        self.wins = 0
        self.losses = 0

        self.generateFirstPlayers()
        self.generateFirstDraft()
    
    def generateFirstPlayers(self):
        numPlayersGenerated = playerCount - numDraftPicks if (self.goodness <= badEnoughForDraftToMatter) else playerCount
        for i in range (numPlayersGenerated):
            self.players.append(player.Player(random.choice(fname) + " " + random.choice(lname), score=(max(0, min(100, self.goodness + math.floor(random.gauss(0, playerSkillDeviation)))))))

    def generateFirstDraft(self):
        if self.goodness <= badEnoughForDraftToMatter:
            for i in range (numDraftPicks):
                self.players.append(player.Player(random.choice(fname) + " " + random.choice(lname), score=(min(100, goodPlayerRating + random.randint(-playerSkillDeviation, playerSkillDeviation)))))
    
    def sortPlayers(self):
        self.players = sorted(self.players, key=lambda player : player.score, reverse=True)

    def getAverageScore(self):
        totalScores = 0
        for player in self.players:
            totalScores += player.score
        return totalScores / len(self.players)

    def win(self):
        self.wins += 1

    def lose(self):
        self.losses += 1 


