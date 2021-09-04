incubators, desiredChicken = list(map(int, input().split()))
daysToChicken = list(map(int, input().split()))

lowerBound = 0
upperBound = 100000000

while lowerBound < upperBound:
   midValue = int((lowerBound + upperBound) / 2)
   totalChicken = 0 
   for cicle in daysToChicken:
      totalChicken += int(midValue / cicle)
   if(totalChicken < desiredChicken):
      lowerBound = midValue + 1
   else:
      upperBound = midValue

print(lowerBound)
   