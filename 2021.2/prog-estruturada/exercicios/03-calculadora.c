#include <stdio.h>

int main(void) {
    float numeroA, numeroB, resultado;
    char operacao;

    printf("\nDigite o primeiro numero: ");
    scanf("%f", &numeroA);
    printf("\nDigite o segundo numero: ");
    scanf("%f", &numeroB);
    printf("\nDigite a operaçao desejada:");
    printf("\n+: soma");
    printf("\n-: subtração");
    printf("\n*: multiplicação");
    printf("\n/: divisão");
    printf("\n==> ");
    scanf(" %c", &operacao);

    switch(operacao) {
        case '+':
            resultado = numeroA + numeroB;
            break;
        case '-':
            resultado = numeroA - numeroB;
            break;
        case '/':
            resultado = numeroA / numeroB;
            break;
        case '*':
            resultado = numeroA * numeroB;
            break;
    }
    printf("\nO resultado é: %.2f\n", resultado);
    return 0;
}