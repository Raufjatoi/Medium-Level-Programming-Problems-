# 8. BMI Calculator:
#  Design a program that calculates the user's Body Mass Index (BMI) based on their weight
# and height.
#  Prompt the user to enter their weight (in kilograms) and height (in meters).
#  Calculate the BMI using the formula: BMI = weight / (height * height).
#  Display the calculated BMI and interpret it based on the standard BMI categories
# (underweight, normal weight, overweight, obese).
w = int(input('Enter ya weight : '))
h = int(input('Enter ya height : '))
f = w / (h * h )
print(f)