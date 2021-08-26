fileName = input()
circle = input().split()
def isInsideCircle(line, circle,file):
  lineX = int(line.split()[0])
  lineY = int(line.split()[1])
  circleX = int(circle[0])
  circleY = int(circle[1])
  radius = int(circle[2])    
  dist = (((lineX - circleX)**2 + (lineY - circleY)**2))**(.5)
  if (dist > radius):
    file.write(line)
    print(f'{lineX} {lineY}')
  return None
with open(f'{fileName}.txt', "r+") as file:
  lines = file.readlines()
  print(f'Pontos do Arquivo {fileName} antes das remoções:')
  for line in lines:
    print(line, end='')
  file.seek(0)
  print(f'\nPontos do Arquivo {fileName} depois das eventuais remoções:')
  for line in lines:
    isInsideCircle(line, circle, file)
    file.truncate() 
file.close()