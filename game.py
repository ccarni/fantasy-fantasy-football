import random

class Game():
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.winningTeam = None

    def playGame(self):
        self.team1.sortPlayers()
        self.team2.sortPlayers()

        # random.gauss adds a normal distribution with a standard deviation of 10
        evaluation = self.team1.getAverageScore() - self.team2.getAverageScore() + random.gauss(0, 10)

        if evaluation > 0:
            self.winningTeam = self.team1
            self.team1.win()
            self.team2.lose()
        else:
            self.winningTeam = self.team2
            self.team1.lose()
            self.team2.win()