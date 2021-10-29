import math

pontoA = input().split(" ")
pontoB = input().split(" ")

x1,y1 = pontoA
x2,y2 = pontoB

distancia = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))