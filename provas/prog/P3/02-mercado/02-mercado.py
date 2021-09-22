fileName = input()
minPrice, maxPrice = list(map(float, input().split()))
dictionary = dict()

def computeLine(line):
    data = line.strip("\n").split('#')
    code = data[0]
    quantity = data[2] 
    price = data[3]
    desc = ' '.join(data[1].split())
    dictData = [f'Descrição: {desc}', f'Qtd: {quantity}', f'Preço: {price}']
    if minPrice <= float(price) <= maxPrice:
        dictionary[code] = list()
        dictionary[code] += dictData
    return None

file = open(f"{fileName}.txt", "r")

for line in file:
    computeLine(line)
file.close()

for index in dictionary:
    print(f'Código: {index}', end='')
    for data in dictionary[index]:
        print(f' {data}', end='')
    print()
