#ask starting annual salary
annual_salary = float(input("What is your annual salary? "))

percent_to_save = .04
months_to_save = 36
semi_annual_raise = 1.07
savings_required = 250000
current_savings = 0.0
steps = 0 
months = 0
guess_high = 10000
guess_low = 0

while current_savings < savings_required:
    for x in range(36):
        if months % 6 == 0:
            annual_salary *= (semi_annual_raise)
        current_savings += (annual_salary*percent_to_save)/12 + current_savings*(0.04/12)
    steps += 1
    
    

print("Number of steps: ", months)
