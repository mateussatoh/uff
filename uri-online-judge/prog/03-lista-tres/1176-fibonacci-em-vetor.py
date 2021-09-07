entriesNumber = int(input())

def computeFibo(fibonacci, entry):
  for iterator in range(2,entry+1):
    fibonacci.append(fibonacci[iterator-2]+fibonacci[iterator-1])
  return fibonacci

for iterator in range(entriesNumber):
    entry = int(input())
    fibonacci=[0,1]
    if entry > 1:
        fibonacciList = computeFibo(fibonacci, entry)
        print(f'Fib({entry}) = {fibonacciList[entry]}')
    if entry <= 1:
        print(f'Fib({entry}) = {fibonacci[entry]}')