call = [1, 1]
fibonacci = [0, 1]
for iterator in range(2, 41):
    call.append(call[iterator-1] + call[iterator-2] + 1)
    fibonacci.append(fibonacci[iterator-1] + fibonacci[iterator-2])
    
entriesNumber = int(input())
for entry in range(entriesNumber):
    number = int(input())
    print(f'fib({number}) = {call[number] -1} calls = {fibonacci[number]}')