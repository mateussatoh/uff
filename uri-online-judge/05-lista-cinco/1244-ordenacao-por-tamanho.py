testsNumber = int(input())
sortedList = []

for test in range(testsNumber):
    test = input().split()
    test = sorted(test, key=len, reverse=True)
    sortedList.append(test)

for item in sortedList:
    for index, word in enumerate(item):
        if index != (len(item) - 1):
            print(word, end=" ")
        else:
            print(word, end="")
    print()
