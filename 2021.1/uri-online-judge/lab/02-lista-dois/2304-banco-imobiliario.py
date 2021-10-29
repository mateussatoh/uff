initialMoney, rounds = list(map(int, input().split()))

ledger = [["D", initialMoney], ["E", initialMoney], ["F", initialMoney]]

for round in range(rounds):
    round = input().split()
    action = round[0]
    if action == "A":
        value = int(round[3])
        for playerInfo in ledger:
            if playerInfo[0] == round[1]:
                playerInfo[1] += value
            elif playerInfo[0] == round[2]:
                playerInfo[1] -= value
    elif action == "C":
        value = int(round[2])
        for playerInfo in ledger:
            if playerInfo[0] == round[1]:
                playerInfo[1] -= value
    elif action == "V":
        value = int(round[2])
        for playerInfo in ledger:
            if playerInfo[0] == round[1]:
                playerInfo[1] += value
print(f'{ledger[0][1]} {ledger[1][1]} {ledger[2][1]}')