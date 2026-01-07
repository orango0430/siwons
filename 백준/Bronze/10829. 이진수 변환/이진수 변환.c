#include<stdio.h>
void print_binary(long long);
int main()
{
	long long num;
	scanf("%lld", &num);
	if (num == 0)
		printf("0");
	print_binary(num);
}
void print_binary(long long n)
{	
	if (n >= 2)
		print_binary(n / 2);
	printf("%lld", n % 2);
	return;
}