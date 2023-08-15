#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: singled list to work with
 *
 * Return: 0 if it is not palindrome otherwise 1
 */

int is_palindrome(listint_t **head)
{
	unsigned int i, dup_len, end_idx, num_node;
	listint_t *start = NULL, *rear = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	start = rear = *head;
	num_node = list_len(start);
	dup_len = num_node * 2;
	end_idx = dup_len - 2;

	for (i = 0; i < dup_len; i = i + 2)
	{
		if (start[i].n != rear[end_idx].n)
			return (0);
		end_idx = end_idx - 2;
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
