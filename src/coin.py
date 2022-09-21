from dataclasses import dataclass, field


@dataclass(order=True)
class Coin:
    """Class to represent a coin. Stores the required counts for solving the change problem using either a Greedy
    algorithm or a Dynamic Programming one.

    Attrs:
        value: the value of the coin
        display: the printable representation of the coin
        count: the final count required to contribute to the total change
        amounts: the intermediary total counts (across all coins) needed when using the dynamic algorithm

    """

    value: int
    display: str = ""
    count: int = 0
    amounts: list = field(default_factory=list)

    def __post_init__(self):
        """Sets the printable representation of the coin"""
        self.display = (
            f"£{int(self.value / 100)}" if self.value % 100 == 0 else f"{self.value}p"
        )

    def __str__(self):
        """Returns the printable representation of the coin along with the number of coins needed"""
        return f"{self.count} x {self.display}"
