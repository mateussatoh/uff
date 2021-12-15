#include <stdio.h>

int main(void) {
    float salary = 1000, interest = 0.001;
    int periodYears;
    
    printf("Quantos anos se passaram desde 1995?: ");
    scanf("%d", &periodYears);
    
    while (periodYears > 0) {
        salary *=  (1.0 + interest);
        interest *= 2.0;
        periodYears--;
    }
    printf("\nO salário atual é: %.2f", salary);
    return 0;
}