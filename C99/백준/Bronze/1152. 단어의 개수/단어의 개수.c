#include<stdio.h>
#include<ctype.h>
#include<stdbool.h>
#define STOP '\n'
int main()
{
	char c;
	int n_words = 0;
	bool word_flag = false;
	while ((c = getchar()) != STOP)
	{
		if (!isspace(c) && word_flag == false)
		{
			n_words++;
			word_flag = true;
		}
		if (isspace(c))
		{
			word_flag = false;
		}
	}
	printf("%d", n_words);
	return 0;
}
