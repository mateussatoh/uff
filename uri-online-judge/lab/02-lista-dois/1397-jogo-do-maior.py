points = []
iterations = 0
roundsNumber = int(input())

while roundsNumber != 0:
    points.append(0)
    points.append(0)
    for round in range(roundsNumber):
        round = list(map(int, input().split()))
        playerA = round[0]
        playerB = round[1]
        if playerA > playerB:
            points[iterations] += 1
        elif playerB > playerA:
            points[iterations + 1] += 1
    iterations += 2
    roundsNumber = int(input())

for index, point in enumerate(points):
    if index % 2 == 0:
        print(f"{points[index]} {points[index+1]}")
