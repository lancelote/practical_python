# pcost.py
#
# Exercise 1.27


def main():
    with open("Data/portfolio.csv", "rt") as portfolio:
        next(portfolio)  # skip header

        total = 0
        for line in portfolio:
            name, shares, price = line.split(",")
            shares = float(shares.strip())
            price = float(price.strip())

            total += shares * price

    print(total)


if __name__ == '__main__':
    main()
