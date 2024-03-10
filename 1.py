# 1. Budget Calculator:
#  Write a program that asks the user for their monthly income and expenses.
#  Calculate the difference between income and expenses.
#  If the difference is positive, display a message indicating how much the user can save.
#  If the difference is negative, display a message indicating how much the user is
# overspending.

#ask the user
monthly_income = int(input('Enter ya monthly income : '))
expense = int(input('Enter ya expense :'))

#cal the diff
diff = (monthly_income - expense)

if monthly_income > expense:
    print(f'you can sav {diff} tha much')
elif monthly_income  < expense :
    print(f'your overspending tha much {diff}')
else:
    print('All avg lagey rhao ustaaaad')
