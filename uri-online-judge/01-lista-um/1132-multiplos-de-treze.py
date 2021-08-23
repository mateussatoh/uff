numeroA = int(input())
numeroB = int(input())

if numeroA > numeroB:
    numeroA, numeroB = numeroB, numeroA
    
somaMultiplos = 0
while numeroA <= numeroB:
    if numeroA % 13 != 0:
        somaMultiplos = somaMultiplos + numeroA
    numeroA = numeroA + 1

print(somaMultiplos)