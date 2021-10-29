boardX = int(input())
boardY = int(input())

boardBorder = boardX + boardY

if boardBorder % 2:
    print(0)
else:
    print(1)
