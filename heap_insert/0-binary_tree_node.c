#include <stdio.h>
#include <stdlib.h>
#include "binary_trees.h"

/**
 * binary_tree_node - creates a binary tree node
 * @parent: pointer to the parent node of the node to create
 * @value: value to put in the new node
 * Return: pointer to the new node, or NULL on failure
 */

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
binary_tree_t *new;

new = malloc(sizeof(binary_tree_t));

if (new == NULL)
{
return (NULL);
}

new->n = value;
new->left = NULL;
new->right = NULL;
new->parent = NULL;

if (parent != NULL)
new->parent = parent;

return (new);
}
