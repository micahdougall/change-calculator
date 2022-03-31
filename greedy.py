from coin import Coin


def greedy_algorithm(amount: float, coins: list[Coin]) -> list[Coin]:
    coins.sort(reverse=True)
    for c in coins:
        c.count = amount // c.value
        amount -= c.count * c.value
    return coins
