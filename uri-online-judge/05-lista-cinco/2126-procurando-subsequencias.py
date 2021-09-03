case = 1
while True:
    try:
        numberA = input()
        numberB = input()
        quantity = numberB.count(numberA)
        print(f'Caso #{case}:')
        if quantity != 0:
            print(f'Qtd.Subsequencias: {quantity}')
            quantity = numberB.rfind(numberA)
            print(f'Pos: {(int(quantity) + 1)}')
        else:
            print('Nao existe subsequencia')
        print()
        case += 1
    except EOFError:
        break