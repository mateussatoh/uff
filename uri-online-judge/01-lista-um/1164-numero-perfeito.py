numeroEntradas = int(input())

for entrada in range(0,numeroEntradas):
    numero = int(input())
    divisor = 1
    divisoesPerfeitas = 0
    while divisor < numero:
        if numero % divisor == 0:
            divisoesPerfeitas = divisoesPerfeitas + divisor
        divisor += 1
    if divisoesPerfeitas == numero:
        print('%d eh perfeito' %(numero))
    else:
        print('%d nao eh perfeito' %(numero))