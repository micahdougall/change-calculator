import argparse
from coin import Coin
import greedy as gd
import dynamic as dy


def select_algorithm(value: int, coinage: list[Coin]) -> list[Coin]:
    gap = 0
    for i in range(1, len(coinage)):
        new_gap = coinage[i].value - coinage[i - 1].value
        if new_gap >= gap:
            print("\nGreedy algorithm not optimal for coin selection. Using dynamic programming...\n")
            return dy.dynamic_programming_algorithm(value, coinage)
    return gd.greedy_algorithm(value, coinage)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Optimum coins selector for any given set of coins and change value.")
    parser.add_argument('value', type=int, help="change value required")
    parser.add_argument('-c', '--coins', nargs='+', type=int,
                        default=[1, 2, 5, 10, 20, 50, 100], help="list of coins available")
    parser.add_argument('-g', '--greedy', action="store_true",
                        help="force the use of a greedy algorithm (quicker but not always optimal)")
    args = parser.parse_args()

    change = args.value
    args.coins.sort()
    coins = [Coin(c) for c in args.coins]

    if args.greedy:
        coins = gd.greedy_algorithm(change, coins)
    else:
        coins = select_algorithm(change, coins)
    if sum((c.count * c.value) for c in coins) == change:
        print("Optimal change:")
        [print(f"\t{(c)}") for c in coins if c.count > 0]
    else:
        print("Unable to supply exact change")