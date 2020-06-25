# mortgage_table.py
#
# Exercise 1.10

principal = 500_000
rate = 0.05
payment = 2684.11
total_paid = 0.0
months_paid = 0

extra_payment = 1000
extra_payment_start_month = 60
extra_payment_end_month = 108

while principal > 0:
    if extra_payment_start_month <= months_paid <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment

    principal = principal * (1 + rate / 12) - payment
    total_paid += payment
    months_paid += 1

    print(f"{months_paid} {total_paid:.2f} {principal:.2f}")

print("total paid", total_paid)
print("months", months_paid)
