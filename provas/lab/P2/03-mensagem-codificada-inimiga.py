message = input()
word = input()
possibleWords = len(message) - len(word) + 1
isInMessage = True
wordsInMessage = 0

for index, iterator in enumerate(range(possibleWords)):
    messageSubstring = message[index : len(word) + index]
    for index, letter in enumerate(range(len(word))):
        if word[index] == messageSubstring[index]:
            isInMessage = False
            break
    if isInMessage == True:
       wordsInMessage += 1
    isInMessage = True
print(wordsInMessage)

