#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list node */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function to push an element onto the stack */
void push(int **stack, int *top, int value) {
    (*top)++;
    (*stack)[*top] = value;
}

/* Function to pop an element from the stack */
int pop(int **stack, int *top) {
    int value = (*stack)[*top];
    (*top)--;
    return value;
}

/* Function to check if a singly linked list is a palindrome */
int is_palindrome(listint_t **head) {
    listint_t *slow = *head;
    listint_t *fast = *head;
    int stack_size = 0;
    int *stack = NULL;
    int top = -1;

    if (*head == NULL)
        return 1; // An empty list is considered a palindrome

    // Find the middle of the linked list using slow and fast pointers
    while (fast != NULL && fast->next != NULL) {
        push(&stack, &top, slow->n);
        slow = slow->next;
        fast = fast->next->next;
        stack_size++;
    }

    // If the list has an odd number of elements, skip the middle element
    if (fast != NULL) {
        slow = slow->next;
        stack_size--;
    }

    // Compare the remaining elements with the elements in the stack
    while (slow != NULL) {
        if (pop(&stack, &top) != slow->n)
            return 0; // Not a palindrome
        slow = slow->next;
        stack_size--;
    }

    // If the stack is empty, it means all elements matched, and it is a palindrome
    return (stack_size == 0) ? 1 : 0;
}

/* Example usage */
int main() {
    listint_t *head = NULL;
    int result;

    // Create a palindrome linked list: 1 -> 2 -> 3 -> 2 -> 1
    head = malloc(sizeof(listint_t));
    head->n = 1;
    head->next = malloc(sizeof(listint_t));
    head->next->n = 2;
    head->next->next = malloc(sizeof(listint_t));
    head->next->next->n = 3;
    head->next->next->next = malloc(sizeof(listint_t));
    head->next->next->next->n = 2;
    head->next->next->next->next = malloc(sizeof(listint_t));
    head->next->next->next->next->n = 1;
    head->next->next->next->next->next = NULL;

    result = is_palindrome(&head);
    printf("Is the linked list a palindrome? %s\n", result ? "Yes" : "No");

    // Free allocated memory
    while (head != NULL) {
        listint_t *temp = head;
        head = head->next;
        free(temp);
    }

    return 0;
}
