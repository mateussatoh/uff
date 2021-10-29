dividendA, divisorA, dividendB, divisorB = list(map(int, input().split()))

fractionDivider = divisorA * divisorB 
fractionDividend = dividendA * divisorB + dividendB * divisorA
possibleDivider = 2

while possibleDivider <= min([fractionDividend, fractionDivider]):
   if (fractionDivider % possibleDivider == 0 and fractionDividend % possibleDivider == 0):
      fractionDividend /= possibleDivider  
      fractionDivider /= possibleDivider  
   else:
      possibleDivider += 1

print(int(fractionDividend), int(fractionDivider))