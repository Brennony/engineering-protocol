#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char *string;

string get_string(const char *prompt)
{
    if (prompt != NULL)
    {
        printf("%s", prompt);
    }

    char buffer[256];
    if (fgets(buffer, sizeof(buffer), stdin) == NULL)
    {
        return NULL;
    }

    size_t len = strlen(buffer);
    while (len > 0 && (buffer[len - 1] == '\n' || buffer[len - 1] == '\r'))
    {
        buffer[--len] = '\0';
    }

    string value = malloc(len + 1);
    if (value == NULL)
    {
        return NULL;
    }

    strcpy(value, buffer);
    return value;
}

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
