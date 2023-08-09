#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle in it
 * @list: the list to be checked
 *
 * Return: 1 if theres a cycle and 0 if there isnt a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list = list, *fast = list;

	if (list == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		/*as long as this runs, the skow runs one time fast while...*/
		/*... the fast runs 2 times faster. they will eventually catch up*/
		if (slow == fast)
			return (1); /*cycle has been detectrd*/
	}
	return (0); /*if no cycle is detected*/
}
