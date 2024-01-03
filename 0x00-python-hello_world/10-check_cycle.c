#include "lists.h"

/**
 * check_cycle - this function that checks if a list has a cycle
 * @list: linked list
 * Retunr: 1 if there is cycle and 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *fst, *slw;
	if (!list || !list->next)
		return (0);
	fst = list;
	slw = list;

	while (slw != NULL && fst != NULL && fst->next != NULL)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
		{
			return (1);
		}
	}
	return (0);
}
