#include "sandpiles.h"

/**
 * print_grid2 - Prints a 3x3 grid
 * @grid: The grid to print
 *
 * Return: void
 */
void print_grid2(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j != 0)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}

/**
 * add - Adds two 3x3 grids
 * @grid1: The first grid to add
 * @grid2: The second grid to add
 *
 * Return: void
 */
void add(int grid1[3][3], int grid2[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
			grid1[i][j] += grid2[i][j];
	}
}

/**
 * tupple - Executes one step of the topple operation on a grid
 * @grid: The grid to analyze
 * @tmp: The grid to store temporary values
 *
 * Return: void
 */
void tupple(int grid[3][3], int tmp[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
			tmp[i][j] = 0;
	}
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid[i][j] > 3)
			{
				tmp[i][j] -= 4;
				if (i + 1 < 3)
					tmp[i + 1][j] += 1;
				if (j + 1 < 3)
					tmp[i][j + 1] += 1;
				if (i - 1 >= 0)
					tmp[i - 1][j] += 1;
				if (j - 1 >= 0)
					tmp[i][j - 1] += 1;
			}
		}
	}
}

/**
 * stable - Checks if a grid is stable
 * @grid: The grid to analyze
 *
 * Return: 1 if the grid is stable, 0 otherwise
 */
int stable(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid[i][j] > 3)
				return (0);
		}
	}
	return (1);
}

/**
 * sandpiles_sum - Adds two 3x3 grids using sandpile addition
 * @grid1: The first grid to add
 * @grid2: The second grid to add
 *
 * Return: void
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int tmp[3][3];

	add(grid1, grid2);
	while (!stable(grid1))
	{
		printf("=\n");
		print_grid2(grid1);
		tupple(grid1, tmp);
		add(grid1, tmp);
	}
}
