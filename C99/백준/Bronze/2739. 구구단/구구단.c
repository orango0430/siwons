#include<stdio.h>
int main(void)
{
	int x = 0;
	int result = 0;

	scanf("%d", &x);
	for (int i = 1; i < 10; i++)
	{
		result = x * i;
		printf("%d * %d = %d\n", x, i, result);
	}
	return 0;
}