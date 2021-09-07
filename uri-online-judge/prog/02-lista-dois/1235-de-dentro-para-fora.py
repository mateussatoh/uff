entriesNumber = int(input())

def invertChar(string):
    charList = list(string)
    splitInvert(charList[::-1])

def splitInvert(invertedList):
     word = ""
     halfLength = int(len(invertedList)/2)
     firstHalf, secondHalf = invertedList[:halfLength], invertedList[halfLength:]
     newList = secondHalf+firstHalf
     for char in newList:
         word += char
     print(word)

for entry in range(entriesNumber):
    entry = str(input())
    invertChar(entry)
