def numberDividers(number):
  for divider in range(1,number+1):
    if number%divider == 0:
      print(divider)

number = int(input())
numberDividers(number)
