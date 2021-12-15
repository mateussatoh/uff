#include <stdio.h>

#define N 3

struct Aluno
{
    char mat[7];
    char nome[40];
    float CR;
    int trancados;
};

typedef struct Aluno aluno;

void preenche(aluno vetorAlunos[N])
{
    int i;

    for (i = 0; i < N; i++)
    {
        printf("\n Digite a matricula: ");
        scanf("%s", &vetorAlunos[i].mat);
        printf("\n Digite o nome: ");
        scanf("%s", &vetorAlunos[i].nome);
        printf("\n Digite o CR: ");
        scanf("%f", &vetorAlunos[i].CR);
        printf("\n Digite os semestres trancados: ");
        scanf("%d", &vetorAlunos[i].trancados);
    }
}

void imprime(aluno vetorAlunos[N])
{
    int i;
    for (i = 0; i < N; i++)
    {
        printf("\n\n---------------------------------");
        printf("\nMATRICULA: ");
        printf("%s", vetorAlunos[i].mat);
        printf("\nNOME: ");
        printf("%s", vetorAlunos[i].nome);
        printf("\nCR: ");
        printf("%f", vetorAlunos[i].CR);
        printf("\nSEMESTRES TRANCADOS: ");
        printf("%d", vetorAlunos[i].trancados);
        printf("\n---------------------------------\n\n");
    }
}

int main(void)
{
    aluno vetorAlunos[N];
    preenche(vetorAlunos);
    imprime(vetorAlunos);
    return 0;
}