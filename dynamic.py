from coin import Coin


def dynamic_programming_algorithm(change: int, coins: list[Coin]) -> list[Coin]:
    coins.sort(reverse=True)
    for i, c in enumerate(coins):
        for t in list(range(0, change + 1)):
            if i == 0:
                if t % c.value == 0:
                    c.amounts.append(t / c.value)
                else:
                    c.amounts.append(float('inf'))
            else:
                if t == 0:
                    c.amounts.append(0)
                else:
                    prev_coin_amount = coins[i - 1].amounts[t]
                    if t < c.value:
                        this_coin_amount = float('inf')
                    else:
                        this_coin_amount = c.amounts[t - c.value] + 1
                    c.amounts.append(min(prev_coin_amount, this_coin_amount))
    return get_coin_selection(change, coins)


def get_coin_selection(change: int, coins: list[Coin]) -> list[Coin]:
    t = change
    i = len(coins) - 1
    while t > 0:
        if i == 0 or coins[i].amounts[t] < coins[i - 1].amounts[t]:
            coins[i].count += 1
            t -= coins[i].value
        else:
            i -= 1
    return coins
