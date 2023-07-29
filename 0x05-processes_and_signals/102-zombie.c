#include <stdio.h>
#include <unistd.h>

/**
 * main - a function that creates five Zombie processes
 *
 * Return: zero
*/
int main(void)
{
	int n;
	pid_t brain;

	for (n = 0; n < 5; n++)
	{
		brain = fork();
		if (!brain)
			return (0);
		printf("Zombie process created, PID: %d\n", brain); }

	while (1)
	{
	sleep(1); }
	return (0);
}
