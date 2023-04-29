import random
import player
import team
import game
from settings import * 

class Runner():
    def __init__(self):
        self.teams = []
        self.superbowlTeams = []
        self.superbowlGames= [] 
        self.openingGames = []
        self.playoffGames = []
        self.playoffTeams = []
    
    def resetNewSeason(self):
        self.superbowlTeams = []
        self.superbowlGames= [] 
        self.openingGames = []
        self.playoffGames = []
        self.playoffTeams = []
    
    def setupTeams(self):
        teamNames = open('teamnames.txt').read().splitlines()
        cityNames = open('citynames.txt').read().splitlines()

        for i in range(teamCount):
            teamIndex = random.randint(0, len(teamNames)-1)
            cityIndex = random.randint(0, len(cityNames)-1)

            self.teams.append(team.Team(f"{cityNames[cityIndex]} {teamNames[teamIndex]}", goodness=random.randint(1, 100)))

            teamNames.pop(teamIndex)
            cityNames.pop(cityIndex)
    
    def setupPlayoffTeams(self):
        # Funky python function sorts all the teams based on wins and then grabs the top 4
        self.playoffTeams = sorted(self.teams, key=lambda team : team.wins, reverse=True)[:4] 
    
    def playOpeningGames(self):
        for i in range(len(self.teams)):
            for j in range(i+1, len(self.teams)):
                self.openingGames.append(game.Game(self.teams[i], self.teams[j]))
                self.openingGames[-1].playGame()
    
    def playPlayoffGames(self):
        for i in range(0, int(len(self.playoffTeams)/2)):
            self.playoffGames.append(game.Game(self.playoffTeams[i], self.playoffTeams[-i-1]))
            self.playoffGames[i].playGame()
            self.superbowlTeams.append(self.playoffGames[i].winningTeam)

    def playSuperbowl(self):
        self.superbowlGames.append(game.Game(self.superbowlTeams[-2], self.superbowlTeams[-1]))
        self.superbowlGames[-1].playGame()