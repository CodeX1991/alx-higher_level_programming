#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: singled list to work with
 *
 * Return: 0 if it is not palindrome otherwise 1
 */

int is_palindrome(listint_t **head)
{
	unsigned int i = 0, j, len, num_node;
	listint_t *start = NULL, *rear = NULL, *temp;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	temp = *head;
	num_node = list_len(temp);

	len = num_node / 2;
	if (num_node % 2 != 0)
		len = (num_node / 2) + 1;

	while (i != len)
	{
		start = rear = *head;
		for (j = 0; j < i; j++)
			start = start->next;

		for (j = 0; j < num_node - (i + 1); j++)
			rear = rear->next;

		if (start->n != rear->n)
			return (0);
		i++;
	}
	return (1);
}

/**
 * list_len - prints all the len=ments of a list_t list
 * @h: the new list created
 *
 * Return: the number of node
 */

size_t list_len(const listint_t *h)
{
	size_t node_num = 0;
	const listint_t *ptr = NULL;

	ptr = h;

	while (ptr != NULL)
	{
		node_num++;
		ptr = ptr->next;
	}
	return (node_num);
}
