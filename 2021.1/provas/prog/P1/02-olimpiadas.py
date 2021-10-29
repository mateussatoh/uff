entriesNumber = int(input())

totalGames = []
countries = []

def computeLine(gameData):
    if gameData[0] not in countries:
            totalGames.append([gameData[0],0,0,0])
            countries.append(gameData[0])
    for game in totalGames:
        if game[0] == gameData[0]:
            if(gameData[1] == 'ouro'):
                game[1] += 1
            if(gameData[1] == 'prata'):
                game[2] += 1
            if(gameData[1] == 'bronze'):
                game[3] += 1
    return None
    
for entry in range(entriesNumber):
    game = str(input())
    gameData = game.split("#")
    computeLine(gameData)

print('Quadro de Medalhas das Olimpíadas de Tóquio:')
for game in totalGames:
    print(f'({game[0]}, {game[1]}, {game[2]}, {game[3]})')

