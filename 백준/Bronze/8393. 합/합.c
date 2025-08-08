#include <stdio.h>

int main()
{
    int a;
    scanf("%d", &a);
    int total = 0;

    for (int i = 0; i < a; i++)
    {
        total += (i + 1);
    }

    printf("%d", total);
    return 0;
}