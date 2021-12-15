#include <stdio.h>

int main(void) {
    float ladoA, ladoB, ladoC;

    printf("\nDigite o primeiro lado: ");
    scanf("%f", &ladoA);
    printf("\nDigite o segundo lado: ");
    scanf("%f", &ladoB);
    printf("\nDigite o terceiro lado: ");
    scanf("%f", &ladoC);

    if (ladoA > ladoB + ladoC || ladoB > ladoA + ladoC || ladoC > ladoB + ladoA){
        printf("\nO triangulo não existe");
    } else {
        if (ladoA == ladoB && ladoB == ladoC) 
            printf("\nO triangulo é equilátero");
        else if (ladoA == ladoB || ladoA == ladoC || ladoB == ladoC) 
            printf("\nO triangulo é isósceles");
        else 
            printf("\nO triangulo é escaleno");
    }
    return 0;

}