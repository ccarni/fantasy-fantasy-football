import runner

season = runner.Runner()

def printResults():
    print(season.superbowlGames[-1].winningTeam.name, season.superbowlGames[-1].winningTeam.goodness)
    print(season.playoffGames)

season.setupTeams()
season.playOpeningGames()
season.setupPlayoffTeams()
season.playPlayoffGames()
season.playSuperbowl()

def runSeason():
    season.resetNewSeason()
    season.playOpeningGames()
    season.setupPlayoffTeams()
    season.playPlayoffGames()
    season.playSuperbowl()

for i in range(50):
    runSeason()

printResults()