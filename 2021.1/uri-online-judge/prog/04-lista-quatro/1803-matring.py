matring = []
result = []

for entry in range(4):
    matring.append(str(input()))

for entry in range(len(matring[0])): 
    asciiNumber = int(matring[3][entry])
    asciiNumber += int(matring[2][entry]) * 10
    asciiNumber += int(matring[1][entry]) * 100
    asciiNumber += int(matring[0][entry]) * 1000
    result.append(asciiNumber)

def decode(result):
  return chr((result[0] * result[entry] + result[-1]) % 257)

for entry in range(1, len(result)-1):
    print(decode(result), end = '')
print()