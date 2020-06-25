# pcost_error_handling.py
#
# Exercise 1.31


def portfolio_cost(filename):
    with open(filename) as portfolio:
        next(portfolio)  # skip header

        total = 0
        for line in portfolio:
            try:
                name, shares, price = line.split(",")
                shares = float(shares.strip())
                price = float(price.strip())

                total += shares * price
            except ValueError as error:
                print(f"failed to process line: {error}")

    return total


def main():
    cost = portfolio_cost('Data/missing.csv')
    print('Total cost:', cost)


if __name__ == '__main__':
    main()
