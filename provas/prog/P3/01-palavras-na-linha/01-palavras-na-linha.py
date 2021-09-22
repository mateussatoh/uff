fileName = input()
minChar, maxChar = list(map(int, input().split()))
dictionary = dict()

def computeLine(line, lineNumber):
    for word in line.strip("\n").split():
        if minChar <= len(word) <= maxChar:
            if word not in dictionary:
                dictionary[word] = set()
            dictionary[word].add(lineNumber)
    lineNumber += 1
    return None

file = open(f"{fileName}.txt", "r")
lineNumber = 1

for line in file:
    computeLine(line, lineNumber)
    lineNumber += 1
file.close()

for word in sorted(dictionary):
    print(f'Chave: {word}')
    if len(dictionary[word]) == 1:
        print('Linha que ela ocorre:')
    else:
        print('Linhas que ela ocorre:')
    for index in dictionary[word]:
        print(f'\t {index}')