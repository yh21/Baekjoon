#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    int arr[1000000] = {1, 2};
    for (int i = 2; i < n; i++)
    {
        arr[i] = (arr[i - 1] + arr[i - 2]) % 15746;
    }

    printf("%d", arr[n - 1]);

    return 0;
}