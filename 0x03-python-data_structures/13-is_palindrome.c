#include <stddef.h>
#include "lists.h"

int compare_lists(listint_t *list1, listint_t *list2);

/**
 * reverse_listint - Reverses a linked list
 * @head: Pointer to the head of the linked list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *mid = NULL;
	int result = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (result);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	prev->next = NULL;
	reverse_listint(&slow);
	result = compare_lists(*head, slow);

	if (mid != NULL)
	{
		prev->next = mid;
		mid->next = slow;
	}
	else
	{
		prev->next = slow;
	}

	return (result);
}

/**
 * compare_lists - Compares two linked lists
 * @list1: Pointer to the head of the first linked list
 * @list2: Pointer to the head of the second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	if (list1 == NULL && list2 == NULL)
		return (1);

	return (0);
}

