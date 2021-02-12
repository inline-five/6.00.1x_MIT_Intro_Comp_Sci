for month in range(12):
    min_payment = balance * monthlyPaymentRate
    unpaid_balance = balance - min_payment
    interest = unpaid_balance * (annualInterestRate / 12.0)
    balance = unpaid_balance + interest


print("Remaining balance: " + str(round((unpaid_balance + interest), 2)))
