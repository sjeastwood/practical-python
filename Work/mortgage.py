# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    if month < 12:
        principal = principal * (1+rate/12) - (1000+payment)
        total_paid = total_paid + payment + 1000
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    month = month + 1


print("Total paid", total_paid)
print("Total number of months", month)
