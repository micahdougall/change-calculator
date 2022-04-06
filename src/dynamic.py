from coin import Coin


def dynamic_programming_algorithm(change: int, coins: list[Coin]) -> list[Coin]:
    """Dynamic algorithm to solve the change problem in the event that the available set of coins does not allow for
    a greedy algorithm to find the optimal solution. Based

    Iterates through the list of coins and, for each value up and to including the amount of change required,
    calculates a count of the total number of coins needed. Stores this total count as a list within each coin (the
    amount attribute). Calls get_coin_selection to determine which particular coins are needed to supply the optimal
    combination of coins.

    Args:
        change: the amount of change required
        coins: the list of available coins

    Returns:
        the list of coins including the count of each coin needed
    """
    coins.sort(reverse=True)
    for i, c in enumerate(coins):
        for t in list(range(0, change + 1)):
            if i == 0:
                if t % c.value == 0:

                    c.amounts.append(t / c.value)
                else:
                    # No solution possible if the first coin doesn't divide the value evenly
                    c.amounts.append(float('inf'))
            else:
                # For zero change value, no coins are needed
                if t == 0:
                    c.amounts.append(0)
                else:
                    # Get the minimum count between the current and previous coin
                    prev_coin_amount = coins[i - 1].amounts[t]
                    if t < c.value:
                        this_coin_amount = float('inf')
                    else:
                        this_coin_amount = c.amounts[t - c.value] + 1
                    c.amounts.append(min(prev_coin_amount, this_coin_amount))
    return get_coin_selection(change, coins)


def get_coin_selection(change: int, coins: list[Coin]) -> list[Coin]:
    """Determines which coins to select based on the stored total count for each value up and to including the change
    required.

    Iterates back through the 'matrix' (all coins and values) from the last coin and maximum value, back down to zero
    to and increments the count of the required coins.

    Args:
        change: the total value of the required change
        coins: the list of coins, which include the total counts as a list attribute (amounts)

    Returns:
        the list of coins, including the final count of each coin required
    """
    t = change
    i = len(coins) - 1
    while t > 0:
        # Compare the total coin count with previous coin
        if i == 0 or coins[i].amounts[t] < coins[i - 1].amounts[t]:
            coins[i].count += 1
            t -= coins[i].value
        else:
            i -= 1
    return coins
