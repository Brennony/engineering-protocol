#include <cs50.h>
#include <stdio.h>


void pyramid(int h);

int main(void)
{
    int h;
    do // Keeps asking until the user gives a height between 1 and 8
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);
    pyramid(h); // Call function to print the pyramid
}

void pyramid(int h)
{
    // CONDITIONALS!
    for (int i = 1; i <= h; i++)
    {
        // For Left Spacing
        for (int j = 0; j < h - i; j++)
        {
            printf(" ");
        }
        // For Left Hashing
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        // For The Gap
        printf("  ");
        // For Right Hashing
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        // Print Next Row
        printf("\n");
    }
}
