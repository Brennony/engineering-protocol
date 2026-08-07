#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Array to assign points to each letter in the english alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string n);

int main(void)
{
    // Get words
    string player1 = get_string("Player 1: ");
    string player2 = get_string("Player 2: ");

    // Compute scores
    int score1 = compute_score(player1);
    int score2 = compute_score(player2);

    // Determine winner and present scores
    printf("P1: %i   P2: %i\n", score1, score2);

    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string n)
{
    int score = 0;
    int len = strlen(n);

    for (int i = 0; i < len; i++)
    {
        if (isupper(n[i]))
        {
            score += POINTS[n[i] - 'A'];
        }
        else if (islower(n[i]))
        {
            score += POINTS[n[i] - 'a'];
        }
    }
    return score;
}
