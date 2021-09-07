entriesNumber = int(input())
totalNumbers = []
results = {}

def countUniqueNumbers(totalNumbers):
  totalNumbers.sort()
  for number in totalNumbers:
      results[number]=totalNumbers.count(number)

  for result in results:
    print(f'{result} aparece {results[result]} vez(es)')


for entry in range(entriesNumber):
  number = int(input())
  totalNumbers.append(number)

countUniqueNumbers(totalNumbers)