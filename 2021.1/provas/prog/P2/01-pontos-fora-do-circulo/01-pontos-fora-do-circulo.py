import os

fileName = input()
circle = input().split()


def isInsideCircle(line, circle, output):
    lineX = int(line.split()[0])
    lineY = int(line.split()[1])
    circleX = int(circle[0])
    circleY = int(circle[1])
    radius = int(circle[2])
    dist = (((lineX - circleX) ** 2 + (lineY - circleY) ** 2)) ** (0.5)
    if dist > radius:
        output.write(f"{lineX} {lineY}\n")
    return None


with open(f"{fileName}.txt", "r") as file:
    with open("newfile.txt", "w") as output:
        print(f"Pontos do Arquivo {fileName} antes das remoções:")
        line = file.readline()
        while line != "":
            print(line.strip("\n"))
            isInsideCircle(line, circle, output)
            line = file.readline()
        os.replace("newfile.txt", f"{fileName}.txt")
file.close()

with open(f"{fileName}.txt", "r") as file:
    print(f"\nPontos do Arquivo {fileName} depois das eventuais remoções:")
    line = file.readline()
    while line != "":
        print(line.strip("\n"))
        line = file.readline()
file.close()
