def countLambs(lambs):  
  return (len(lambs) - (len(lambs) - len(set(lambs)))) 

for entry in range(int(input())):
  input()
  lambs = input().split(' ')
  print(countLambs(lambs))
