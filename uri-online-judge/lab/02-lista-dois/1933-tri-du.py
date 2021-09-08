cardA, cardB = list(map(int, input().split()))

if cardA == cardB:
    print(cardA)
elif cardA > cardB:
    print(cardA)
else:
    print(cardB)
