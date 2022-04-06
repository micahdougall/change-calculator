# Change Calculator

Program to calculate the optimal combination of coins (the fewest total number) to supply a change value.

Uses one of two available algorithms:

- `Greedy` :arrow_right: chooses locally optimal solutions to build up global solution
- `Dynamic Programming` :arrow_right: mathematically optimal for any problem, regardless of coin selection

Depending on the available coins, the program will determine the optimum algorithm and return a print out of the coins required.


## Usage

Prerequisites: `Python3`

The command-line arguments include a required argument for the value of the change, eg:

    py main.py 87

In this case, the program uses the available UK sterling coins, i.e. 1, 2, 5, 10, 20, 50, £1 and £2.

Alternatively, the list of coins can be passed as an additional argument (--coins or -c)

    py main.py 87 -c 1 2 5 6

Finally, an argument can be passed to force the program to use the greedy algorithm, i.e.:

    py main.py 87 -g

Which will force to the program to use the (quicker) greedy algorithm but will not necessarily provide the optimal solution.