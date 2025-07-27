#include <stdio.h>
void numbers(int a, int b);

int main()
{
    while(1)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        if (a == 0)
            break;
        else
            numbers(a, b);
    }
}

void numbers(int a, int b)
{
    if (a > b)
    {
        if (a % b == 0)
            printf("multiple\n");
        else
            printf("neither\n");
    }
    else
    {
        if (b % a == 0)
            printf("factor\n");
        else
            printf("neither\n");
    }
}