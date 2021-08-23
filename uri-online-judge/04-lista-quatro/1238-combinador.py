def combinator(entry):
  string = ''
  wordDiff = abs(len(entry[0]) - len(entry[1]))
  biggerWord = entry[0]
  if(len(entry[1]) > len(entry[0])):
    biggerWord = entry[1]
  for letterIndex in range(len(biggerWord) - wordDiff):
    string += entry[0][letterIndex]
    string += entry[1][letterIndex]
  if(len(entry[0]) != len(entry[1])):
    string += biggerWord[-wordDiff:]
  return string
    
for entry in range(int(input())):
  print(combinator(input().split()))