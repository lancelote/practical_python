# pcost_function.py
#
# Exercise 1.30


def portfolio_cost(filename):
    with open(filename) as portfolio:
        next(portfolio)  # skip header

        total = 0
        for line in portfolio:
            name, shares, price = line.split(",")
            shares = float(shares.strip())
            price = float(price.strip())

            total += shares * price

    return total


def main():
    cost = portfolio_cost('Data/portfolio.csv')
    print('Total cost:', cost)


if __name__ == '__main__':
    main()
