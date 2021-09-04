packetsInt = input()
marginA = list(map(int, input().split()))
marginA.sort()

diffPackets = [marginA[i+1]-marginA[i] for i in range(len(marginA)-1)]
minA = min(marginA)
impossibleCrossing = False

for diff in diffPackets:
   if diff > 8:
      impossibleCrossing = True

if minA <= 8 and impossibleCrossing == False:
   print('S')
else:
   print('N') 
