# mortgage_overpayment.py
#
# Exercise 1.11

principal = 500_000
rate = 0.05
payment = 2684.11
total_paid = 0.0
months_paid = 0

extra_payment = 1000
extra_payment_start_month = 60
extra_payment_end_month = 108

while principal > 0:
    current_month_payment = payment

    if extra_payment_start_month <= months_paid <= extra_payment_end_month:
        current_month_payment += extra_payment

    principal = principal * (1 + rate / 12)
    current_month_payment = min(current_month_payment, principal)
    principal -= current_month_payment
    total_paid += current_month_payment
    months_paid += 1

    print(f"{months_paid:03} {total_paid:>9.2f} {principal:>9.2f}")

print("total paid", total_paid)
print("months", months_paid)
