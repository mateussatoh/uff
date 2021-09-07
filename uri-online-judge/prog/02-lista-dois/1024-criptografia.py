entriesNumber = int(input())

def firstCrypt(entry):
    asciiString = ''
    for char in entry:
        if (char.isalpha() == True):
            asciiString += chr(ord(char) + 3)
        else:
            asciiString += char
    secondCrypt(asciiString)

def secondCrypt(asciiString):
     finalCrypt(asciiString[::-1])

def finalCrypt(asciiString):
    halfLength = int(len(asciiString)/2)
    firstHalf, secondHalf = asciiString[:halfLength], asciiString[halfLength:]
    newSecondHalf = ""
    for char in secondHalf:
        newSecondHalf += chr(ord(char) - 1)
    print(firstHalf + newSecondHalf)

for entry in range(entriesNumber):
    entry = str(input())
    firstCrypt(entry)
