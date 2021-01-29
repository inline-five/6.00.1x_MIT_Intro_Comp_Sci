#ask starting annual salary
annual_salary = float(input("What is your annual salary? "))
# portion of salary to be saved
portion_saved = float(input("What portion of salary will be saved? "))
# cost of dream home
total_cost = float(input("What is the cost of your dream home? "))
# semi-annual raise increased every 6 months
semi_annual_raise = float(input("What is your semi-annual raise? "))

portion_down_payment = total_cost * 0.25
current_savings = 0.0
months = 0

while current_savings < portion_down_payment:
    current_savings += portion_saved * annual_salary/12 + current_savings*.04/12
    months += 1
    if months % 6 == 0:
        annual_salary *= (semi_annual_raise + 1)

print("Number of months:", months)
