#include "lists.h"

/**
 * check_cycle - check the cycle in linked list listint
 * @list: the list tobe checked
 *
 * Return: 0 if there is no cycle, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	turtle = hare = list;
	while (turtle && hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;

		if (turtle == hare)
			return (1);
	}
	return (0);
}
