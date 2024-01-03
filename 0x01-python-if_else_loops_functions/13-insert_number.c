#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stddef.h>

/**
 * instert_node - insterts a nuber into a sorted list
 * @head: a linked list
 * @number: number to be entered
 * Return: ptr to the new head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

		if (!head)
			return (NULL);

		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);
	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (old && old->n <number)
		{
			temp = old;
			old = old->next;
		}
		temp->next = new;
		new->next = old;
	}
	return (new);
}
