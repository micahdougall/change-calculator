from dataclasses import dataclass, field


@dataclass(order=True)
class Coin:
    value: int
    display: str = ""
    count: int = 0
    amounts: list = field(default_factory=list)

    def __post_init__(self):
        if self.value % 100 == 0:
            self.display = f"£{int(self.value / 100)}"
        else:
            self.display = f"{self.value}p"

    def __str__(self):
        return f"{self.count} x {self.display}"
