list=[]

for iterator in range(100):
    entry = float(input())
    list.append(entry)
    if entry <= 10:
        print(f'A[{iterator}] = {entry}')