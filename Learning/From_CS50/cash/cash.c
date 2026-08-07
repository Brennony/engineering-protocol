#include <cs50.h>
#include <math.h>
#include <stdio.h>

void change_due(int coins);

int main(void)
{
    // Loops based on if user inputs number >= 1
    int coins;
    do
    {
        coins = get_int("Change owed: ");
    }
    while (coins <= 0);
    change_due(coins);
}

void change_due(int coins)
{
    // Basic mathematics
    int coin = 0;

    // Part A: Quarters
    coin += coins / 25;
    coins %= 25;

    // Part B: Dimes
    coin += coins / 10;
    coins %= 10;

    // Part C: Nickels
    coin += coins / 5;
    coins %= 5;

    // Part D: Pennies
    coin += coins;

    printf("%i\n", coin);
}
