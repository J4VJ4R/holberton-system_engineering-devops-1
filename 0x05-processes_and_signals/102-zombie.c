#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - function that let get bussy the main
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * _fork - function that create a child process
 *
 * Return: Nothing
 */
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

/**
 * main - main test function
 *
 * Return: Always 0
 */
int main(void)
{
	_fork();
	_fork();
	_fork();
	_fork();
	_fork();
	infinite_while();
	return (EXIT_SUCCESS);
}
