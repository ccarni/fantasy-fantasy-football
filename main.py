from array import *
import random
import math
import player
import team
from settings import *


cityNames = open('citynames.txt').read().splitlines()
teamNames = open('teamnames.txt').read().splitlines()
teams = []


# Set up teams
for i in range(teamCount):
    teamIndex = random.randint(0, len(teamNames)-1)
    cityIndex = random.randint(0, len(cityNames)-1)

    teams.append(team.Team(f"{cityNames[cityIndex]} {teamNames[teamIndex]}" ,goodness=random.randint(1, 100))) 

    teamNames.pop(teamIndex)
    cityNames.pop(cityIndex)
    
def runGame(team1, team2):
    team1.sortPlayers()
    team2.sortPlayers()

    # random.gauss adds a normal distribution with a standard deviation of 10
    evaluation = team1.getAverageScore() - team2.getAverageScore() + random.gauss(0, 10)

    return evaluation




_evaluation = runGame(teams[0], teams[7])
scoreStart = random.randint(6, 30)

print(teams[0].goodness, teams[7].goodness)

if _evaluation > 0:
    print("team 1 wins")
else:
    print("team 2 wins")


