#include <stdio.h>

int main(void) {
    int iterator, totalNumeros, soma3 = 0, cont3 = 0, soma2 = 0, num;
    
    printf("Digite um valor para totalNumeros: ");
    scanf("%d", &totalNumeros);
    
    for (iterator = 1; iterator <= totalNumeros; iterator++) {
        printf("\n Digite um número: ");
        scanf("%d", &num);
        if (num%2 == 0)
            soma2 += num;
        if (num%3 == 0) {
            soma3 += num;
            cont3++;
        }
    }
    printf("\nA soma dos números pares é: %d", soma2);
    printf("\nA média dos mult de 3 é: %f", soma3/(cont3*1.0));
    return 0;
}