monthly_payment = balance / 12
high = balance
low = monthly_payment
initial_balance = balance

while abs(balance) > 1:

    for month in range(12):
        unpaid_balance = balance - monthly_payment
        interest = unpaid_balance * (annualInterestRate / 12.0)
        balance = unpaid_balance + interest
        if balance < -10:
            break
    
    if balance > 1:
        low = monthly_payment
        monthly_payment = (low + high) / 2
        balance = initial_balance
    elif balance < -1:
        high = monthly_payment
        monthly_payment = (low + high) / 2
        balance = initial_balance
    elif abs(balance) <= 1:
        break

monthly_payment = (int(monthly_payment / 10) + 1) * 10
print("Lowest payment: " + str(round(monthly_payment)))
