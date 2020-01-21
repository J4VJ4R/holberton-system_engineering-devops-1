#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

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
 * Return: 0 in child, other for father
 */
int _fork(void)
{
pid_t ret;

	ret = fork();
	if (ret == 0)
	{
		sleep(1);
		return(0);
	}
	else
	{
		printf("Zombie process created, PID: %d\n", ret);
		return (ret);
	}
}

/**
 * main - main test function
 *
 * Return: Always 0
 */
int main(void)
{
	if (_fork() == 0)
		return (0);
	if (_fork() == 0)
		return (0);
	if (_fork() == 0)
		return (0);
	if (_fork() == 0)
		return (0);
	if (_fork() == 0)
		return (0);
	if (_fork() == 0)
		return (0);
	infinite_while();
	return (EXIT_SUCCESS);
}
