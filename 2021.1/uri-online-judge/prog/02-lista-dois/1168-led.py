entriesNumber = int(input())

def getLedsNumber(number):
    numberList = list(number)
    ledNumber = 0
    for numberChar in numberList:
        if numberChar == '0' or numberChar == '9' or numberChar == '6':
            ledNumber += 6
        if numberChar == '1':
            ledNumber += 2
        if numberChar == '2' or numberChar == '3':
            ledNumber += 5
        if numberChar == '4':
            ledNumber += 4
        if numberChar == '5':
            ledNumber += 5
        if numberChar == '7':
            ledNumber += 3
        if numberChar == '8':
            ledNumber += 7
    print(str(ledNumber) + " leds")

for entry in range(entriesNumber):
    entry = str(input())
    getLedsNumber(entry)
