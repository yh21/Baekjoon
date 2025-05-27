#include <stdio.h>

int main()
{
    int a;
    int b;
    scanf("%d", &a);
    scanf("%d", &b);
    
    if ((a > 0) && (b > 0))
        printf("1");
    else if ((a > 0) && (b < 0))
        printf("4");
    else if ((a < 0) && (b > 0))
        printf("2");
    else
        printf("3");
    
    return 0;
}