def computeWords(totalWords):  
    onlyOneMatch = []
    for word in totalWords:
        if word not in onlyOneMatch and word:
            onlyOneMatch.append(word)
    return onlyOneMatch

def newLine(totalWords):
    line = input()
    words = line.split(' ')
    if line:
        totalWords.extend(words)
        newLine(totalWords)
    else:
        for word in computeWords(totalWords):
            print(word)
    return None

totalWords = []
newLine(totalWords)
