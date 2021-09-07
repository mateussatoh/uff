list=[]

for iterator in range(20):
    entry=int(input())
    list.append(entry)

sandwithSwap = list[::-1]

for iterator in range(20):
    print(f'N[{iterator}] = {sandwithSwap[iterator]}')