def paulasGame(entry):
  if(entry[0] == entry[2]):
    return int(entry[0]) * int(entry[2])
  elif(entry[1].isupper()):
    return int(entry[2]) - int(entry[0])
  elif(entry[1].islower()):
    return int(entry[0]) + int(entry[2])

for entry in range(int(input())):
    print(paulasGame(list(input())))