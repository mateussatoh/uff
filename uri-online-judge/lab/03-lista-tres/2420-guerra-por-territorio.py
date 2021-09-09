dummy = input()

areas = list(map(int, input().split()))
halfTotalArea = sum(areas) / 2
newArea = 0

for index, area in enumerate(areas):
   if(newArea != halfTotalArea):
      newArea += area
   else:
      print(index)
      break
