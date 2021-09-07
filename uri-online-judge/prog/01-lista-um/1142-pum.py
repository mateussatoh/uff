numeroLinhas = int(input())
valorInicial = 1

for linha in range(0, numeroLinhas):
    print('%d %d %d PUM' %(valorInicial,valorInicial+1,valorInicial+2))
    valorInicial += 4