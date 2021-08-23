totalValues = []
index = 0

for entry in range(0,10):
  value = int(input())
  totalValues.append(value)
  if value <= 0:
    value = 1
  print(f'X[{index}] = {value}')
  index += 1
