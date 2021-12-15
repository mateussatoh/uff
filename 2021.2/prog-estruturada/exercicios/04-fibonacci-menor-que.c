#include <stdio.h>

int main(void) {
    int numeroMax, nextFibo = 1, prevFibo = 1, temp;
    printf("Digite o número máximo da série: ");
    scanf("%d", &numeroMax);
    printf("%d %d ", prevFibo, nextFibo);
    while (nextFibo < numeroMax) {
        temp = nextFibo;
        nextFibo += prevFibo;
        prevFibo = temp;
        if (nextFibo < numeroMax) {
            printf("%d ", nextFibo);
        }
    }
    return 0;
}