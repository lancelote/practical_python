# extra_payment.py
#
# Exercise 1.8

principal = 500_000
rate = 0.05
payment = 2684.11
total_paid = 0.0
months_paid = 0

while principal > 0:
    if months_paid < 12:
        principal -= 1000
        total_paid += 1000

    principal = principal * (1 + rate / 12) - payment
    total_paid += payment
    months_paid += 1

print("total paid", total_paid)
print("months", months_paid)
