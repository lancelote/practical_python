# pcost_args.py
#
# Exercise 1.33

import csv
import sys


def portfolio_cost(filename: str) -> float:
    with open(filename) as portfolio:
        rows = csv.reader(portfolio)

        # skip header
        _ = next(rows)

        total = 0
        for (name, shares, price) in rows:
            try:
                total += float(shares) * float(price)
            except ValueError as error:
                print(f"failed to process line: {error}")

    return total


def main() -> None:
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        file_path = "data/missing.csv"
    cost = portfolio_cost(file_path)
    print("Total cost:", cost)


if __name__ == "__main__":
    main()
