from array import *
import random
import math
import player
import team
from settings import *
import game


cityNames = open('citynames.txt').read().splitlines()
teamNames = open('teamnames.txt').read().splitlines()
teams = []
openingGames = []


def setupTeams():
    for i in range(teamCount):
        teamIndex = random.randint(0, len(teamNames)-1)
        cityIndex = random.randint(0, len(cityNames)-1)

        teams.append(team.Team(f"{cityNames[cityIndex]} {teamNames[teamIndex]}" ,goodness=random.randint(1, 100))) 

        teamNames.pop(teamIndex)
        cityNames.pop(cityIndex)
    

def playOpeningGames():
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            openingGames.append(game.Game(teams[i], teams[j]))
            openingGames[-1].playGame()

def getPlayoffTeams():
    # grabs the first four teams
    _playoffTeams = teams[:4]

    # sorts _playoffTeams


    # Checks each other team, seeing if they are good enough to be in the top 4 and if so ranking them relatively
    for i in range(5, len(teams)):
        for j in range(4):
            if (teams[i].wins > _playoffTeams[j].wins) and (not teams[i] in _playoffTeams):
                _playoffTeams[j] = teams[i]
    return _playoffTeams
                
setupTeams()
playOpeningGames()
playoffTeams = getPlayoffTeams()
# playPlayoffs()

# print opening games
print("="*100)
for k in range(len(teams)):
    print(teams[k].wins, teams[k].losses, teams[k].goodness)

print("="*50)
for team in playoffTeams:
    print(team.name, team.goodness, team.wins)

