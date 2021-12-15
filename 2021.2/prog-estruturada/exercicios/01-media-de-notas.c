#include <stdio.h>

int main(void) {
    float notaA, notaB, notaC , media;

    printf("\nDigite a primeira nota: ");
    scanf("%f", &notaA);
    printf("\nDigite a segunda nota: ");
    scanf("%f", &notaB);
    printf("\nDigite a terceira nota: ");
    scanf("%f", &notaC);

    media = (notaA + notaB + notaC) / 3;
    printf("\nSua média é: %.2f\n", media);

    return 0;
}