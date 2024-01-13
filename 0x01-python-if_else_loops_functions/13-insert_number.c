#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node, *current, *prev;

    /* Allocate memory for the new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        return NULL; /* Allocation failed */
    }

    new_node->n = number;
    new_node->next = NULL;

    current = *head;
    prev = NULL;

    /* Traverse the list to find the correct position to insert the new node */
    while (current != NULL && current->n < number) {
        prev = current;
        current = current->next;
    }

    /* Insert the new node */
    if (prev == NULL) {
        /* Insert at the beginning of the list */
        new_node->next = *head;
        *head = new_node;
    } else {
        /* Insert in the middle or at the end of the list */
        prev->next = new_node;
        new_node->next = current;
    }

    return new_node;
}
