numbers = input().split(" ")
numberA, numberB, numberC = numbers

def returnGreater(value1,value2):
  return ((int(value1)+int(value2)+abs(int(value1)-int(value2)))/2)
    
def compareABC(a,b,c):
   return returnGreater(returnGreater(a,b),c)

print("%d eh o maior" % compareABC(numberA, numberB, numberC))