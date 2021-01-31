annual_salary = float(input("What is your annual salary? "))

PERCENT_TO_SAVE = 10000
MONTHS_TO_SAVE = 36
SEMI_ANNUAL_RAISE = 1.07
SAVINGS_REQD = 250000
initial_salary = annual_salary
current_savings = 0.0
steps = 0 
guess_high = 10000
guess_low = 0

for months in range(1, MONTHS_TO_SAVE + 1):
    current_savings += round((annual_salary*(PERCENT_TO_SAVE / 10000))/12 + current_savings*(0.04/12), 2)
    if months % 6 == 0:
        annual_salary *= (SEMI_ANNUAL_RAISE)

if current_savings < SAVINGS_REQD:
    print("It is not possible to save that amount.")

else:
    steps += 1
    while abs(current_savings - SAVINGS_REQD) > 100:
        if PERCENT_TO_SAVE == 0:
            break
        current_savings = 0.0
        annual_salary = initial_salary
        PERCENT_TO_SAVE = int((guess_high + guess_low) / 2)

        for months in range(1, MONTHS_TO_SAVE + 1):
            current_savings += round((annual_salary*(PERCENT_TO_SAVE / 10000))/12 + current_savings*(0.04/12), 2)
            if months % 6 == 0:
                annual_salary *= (SEMI_ANNUAL_RAISE)
            elif current_savings > SAVINGS_REQD:
                break
        steps += 1

        if abs(current_savings - SAVINGS_REQD) < 100:
            break
        elif current_savings > SAVINGS_REQD and PERCENT_TO_SAVE > 0:
            guess_high = PERCENT_TO_SAVE
        elif current_savings < SAVINGS_REQD:
            guess_low = PERCENT_TO_SAVE 

    print("Best savings rate: {}\nNumber of steps: {}".format(round(PERCENT_TO_SAVE/10000,4), steps))
