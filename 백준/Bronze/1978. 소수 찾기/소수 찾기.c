#include<stdio.h>
int main()
{
	int num; //입력받는 수의 개수
	int arr[100]; //수 저장배열
	int b = 0;
	int a;
	scanf("%d", &num);
	for (int i = 0; i < num; i++) //수의 개수만큼 반복 입력
	{
		scanf("%d", &arr[i]);
	}
	for (int i = 0; i < num; i++)
	{
		a = 0;
		for (int j = 0; j < arr[i]; j++)
		{
			if (arr[i] % (j + 1) == 0)
			{
				a += 1;
			}
		}
		if (a == 2)
		{
			b += 1;
		}
	}
printf("%d", b);
return 0;
}