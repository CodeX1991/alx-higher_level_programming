#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the list to work with
 * @number: the number to insert
 *
 * Return: the address of the new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL, *current_node = NULL, *new_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head)
	{
		current_node = *head;
		if (number <= current_node->n)
		{
			new_node->next = current_node;
			*head = new_node;
		}
		else
		{
			while (current_node->next)
			{
				if (number <= current_node->next->n)
				{
					temp = current_node->next;
					current_node->next = new_node;
					new_node->next = temp;
					return (*head);
				}
				current_node = current_node->next;
			}
			temp = current_node->next;
			current_node->next = new_node;
			new_node->next = temp;
		}
		return (*head);
	}
	new_node->next = NULL;
	*head = new_node;
	return (*head);
}
