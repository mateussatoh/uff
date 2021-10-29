entry = int(input())

numbers = input()
numbers = numbers.split()

for iterator in range(len(numbers)):
    numbers[iterator] = int(numbers[iterator])

def computeSmaller(numbers):
  smaller = numbers[0]
  index = 0
  for iterator in range(1,len(numbers)):
      if numbers[iterator] < smaller:
          smaller = numbers[iterator]
          index = iterator
  print(f'Menor valor: {smaller}')
  print(f'Posicao: {index}')
  
computeSmaller(numbers)


