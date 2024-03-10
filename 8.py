# 8. BMI Calculator:
#  Design a program that calculates the user's Body Mass Index (BMI) based on their weight
# and height.
#  Prompt the user to enter their weight (in kilograms) and height (in meters).
#  Calculate the BMI using the formula: BMI = weight / (height * height).
#  Display the calculated BMI and interpret it based on the standard BMI categories
# (underweight, normal weight, overweight, obese).
# Prompt the user to enter their weight (in kilograms) and height (in meters)

weight = float(input('Enter your weight in kilograms: '))
height = float(input('Enter your height in meters: '))


bmi = weight / (height * height)
print('Your BMI is:', bmi)

if bmi < 18.5:
    print('You are underweight.')
elif bmi < 25:
    print('You have a normal weight.')
elif bmi < 30:
    print('You are overweight.')
else:
    print('You are obese.')
