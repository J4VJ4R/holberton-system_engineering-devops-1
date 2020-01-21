#include <stdio.h>
#include <stdlib.h>

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

void _fork(void) 
{ 
int ret;

	ret = fork();
	if (ret == 0) 
	{
		sleep(1); 
		exit(0);
	}
	else
		printf("Zombie process created, PID: %d\n", ret); 
} 

int main()
{
	_fork();
	_fork();
	_fork();
	_fork();
	_fork();
	infinite_while();
	return (EXIT_SUCCESS);
}
