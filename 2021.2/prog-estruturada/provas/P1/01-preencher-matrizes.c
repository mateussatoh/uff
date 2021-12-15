#include <stdio.h>
#include <stdlib.h>

#define lines 2
#define columns 2

void preencheMat(int matrix[lines][columns])
{
    int lineIterator, columnIterator;
    printf("\n\nPreenchendo a Matriz\n");
    for (lineIterator = 0; lineIterator < lines; lineIterator++)
    {
        for (columnIterator = 0; columnIterator < columns; columnIterator++)
        {
            printf("Digite a posicao [%d][%d]: ", lineIterator, columnIterator);
            scanf("%d", &matrix[lineIterator][columnIterator]);
        }
    }
}

void escreveMat(int mat[lines][columns])
{
    int lineIterator, columnIterator;
    printf("\n\nA matriz é: \n");
    for (lineIterator = 0; lineIterator < lines; lineIterator++)
    {
        for (columnIterator = 0; columnIterator < columns; columnIterator++)
        {
            printf("%d ", mat[lineIterator][columnIterator]);
        }
        printf("\n");
    }
    printf("\n");
}

void somaMat(int A[lines][columns], int B[lines][columns], int C[lines][columns])
{
    int lineIterator, columnIterator;
    for (lineIterator = 0; lineIterator < lines; lineIterator++)
    {
        for (columnIterator = 0; columnIterator < columns; columnIterator++)
        {
            C[lineIterator][columnIterator] = A[lineIterator][columnIterator] + B[lineIterator][columnIterator];
        }
    }
    escreveMat(C);
}

void subtrairMat(int A[lines][columns], int B[lines][columns], int C[lines][columns])
{
    int lineIterator, columnIterator;
    for (lineIterator = 0; lineIterator < lines; lineIterator++)
    {
        for (columnIterator = 0; columnIterator < columns; columnIterator++)
        {
            C[lineIterator][columnIterator] = A[lineIterator][columnIterator] - B[lineIterator][columnIterator];
        }
    }
    escreveMat(C);
}

void multiplicaMat(int A[lines][columns], int B[lines][columns], int C[lines][columns])
{
    int elements = lines * columns;
    int lineIteratorA, linesIteratorB, columnIteratorB;
    for (lineIteratorA = 0; lineIteratorA < lines; lineIteratorA++)
    {
        for (columnIteratorB = 0; columnIteratorB < columns; columnIteratorB++)
        {
            for (linesIteratorB = 0; linesIteratorB < lines; linesIteratorB++)
            {
                C[lineIteratorA][columnIteratorB] += A[lineIteratorA][linesIteratorB] * B[linesIteratorB][columnIteratorB];
            }
        }
    }
    escreveMat(C);
}

void menu(void)
{
    printf("\n\nMENU: \n");
    printf("1 – (A + B)\n");
    printf("2 – (A – B)\n");
    printf("3 – (A x B)\n");
    printf("4 – Fim do programa\n");
}

int main(void)
{
    int matrixA[lines][columns];
    int matrixB[lines][columns];
    int result[lines][columns];

    char op;

    preencheMat(matrixA);
    preencheMat(matrixB);
    escreveMat(matrixA);
    escreveMat(matrixB);

    menu();

    //Zerar o C para evitar erros
    int lineIteratorC, columnIteratorC;
    for (lineIteratorC = 0; lineIteratorC < lines; lineIteratorC++)
    {
        for (columnIteratorC = 0; columnIteratorC < columns; columnIteratorC++)
        {
            result[lineIteratorC][columnIteratorC] = 0;
        }
    }

    scanf(" %c", &op);

    switch (op)
    {
    case '1':
        somaMat(matrixA, matrixB, result);
        break;
    case '2':
        subtrairMat(matrixA, matrixB, result);
        break;
    case '3':
        multiplicaMat(matrixA, matrixB, result);
        break;
    case '4':
        exit(0);
        break;
    }
    return 0;
}