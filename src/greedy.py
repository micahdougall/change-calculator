from coin import Coin


def greedy_algorithm(amount: float, coins: list[Coin]) -> list[Coin]:
    """Greedy algorithm which optimally solves the change problem with a simpler and less expensive solution than the
    greedy algorithm. Only works for change problems which have the Greedy Choice and Optimal Substructure properties
    (e.g. the set of available coins in UK sterling).

    Args:
        amount: the amount of change required
        coins: the list of available coins

    Returns:
        the list of coins including the count of each coin needed

    """
    coins.sort(reverse=True)  # List of coins must in descending order
    for c in coins:
        c.count = amount // c.value
        amount -= c.count * c.value
    return coins
