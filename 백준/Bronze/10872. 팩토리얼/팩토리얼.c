#include<stdio.h>
int factorial(int);
int main()
{
	int a;
	int b;
	scanf("%d", &a);
	b = factorial(a);
	printf("%d", b);

}
int factorial(int n)
{
	
	if (n <= 1)
		return 1;
	else
		return n * factorial(n - 1);
	
}