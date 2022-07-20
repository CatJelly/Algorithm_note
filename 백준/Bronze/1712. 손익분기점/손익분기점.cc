#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void)
{

    long A, B, C, cnt = -1;
    scanf("%ld %ld %ld", &A, &B, &C);
    if (B < C)
    {
        cnt = A / (C - B) + 1;
    }
    else
    {
        cnt = -1;
    }
    printf("%ld\n", cnt);
}