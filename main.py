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
superbowlTeams = []
superbowlGame = None
openingGames = []
playoffGames = []


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
    # funky python magic
    sortedTeams = sorted(teams, key=lambda team : team.wins, reverse=True)
    return sortedTeams[:4]

# ONLY WORKS FOR AN EVEN NUMBER OF TEAMS
def playPlayoffs():
    for i in range(0, int(len(playoffTeams)/2)):
        playoffGames.append(game.Game(playoffTeams[i], playoffTeams[-i - 1]))
        playoffGames[i].playGame()
        superbowlTeams.append(playoffGames[i].winningTeam)

def playSuperbowl():
    # print("Super bowl time. Teams: " + superbowlTeams[0].name + ", " + superbowlTeams[1].name)
    superbowlGame = game.Game(superbowlTeams[0], superbowlTeams[1])
    superbowlGame.playGame()
    # print("-"*50)
    # print("Super epic game winner: " + superbowlGame.winningTeam.name +"||| score: " + str(superbowlGame.winningTeam.goodness))

    return superbowlGame

setupTeams()
playOpeningGames()
playoffTeams = getPlayoffTeams()
playPlayoffs()
superbowlGame = playSuperbowl()

print(superbowlGame.winningTeam.goodness)
                
while not superbowlGame.winningTeam.goodness <= 15:
    cityNames = open('citynames.txt').read().splitlines()
    teamNames = open('teamnames.txt').read().splitlines()
    teams = []
    superbowlTeams = []
    superbowlGame = None
    openingGames = []
    playoffGames = []
    
    setupTeams()
    playOpeningGames()
    playoffTeams = getPlayoffTeams()
    playPlayoffs()
    superbowlGame = playSuperbowl()
    print(superbowlGame.winningTeam.goodness)

# print all teams
print("="*50)
print("Teams: ")
for team in teams:
    print(team.name, team.goodness, "|", team.wins, team.losses)

print ("-"*50)
print("Playoff teams:")
for team in playoffTeams:
    print(team.name, team.goodness, "|", team.wins, team.losses)


print ("-"*50)
print("Superbowl!!!!:")
for team in superbowlTeams:
    print(team.name, team.goodness, "|", team.wins, team.losses)

print("-"*50)
print("winning team")
for player in superbowlGame.winningTeam.players:
    print(player.name, player.score)

# print opening games
# print("="*100)
# for k in range(len(teams)):
#     print(teams[k].wins, teams[k].losses, teams[k].goodness)
# print("="*50)
# for team in playoffTeams:
#     print(team.name, team.goodness, team.wins)

