# pcost_library.py
#
# Exercise 1.32

import csv


def portfolio_cost(filename):
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


def main():
    cost = portfolio_cost('Data/missing.csv')
    print('Total cost:', cost)


if __name__ == '__main__':
    main()
