# 7. Temperature Converter:
#  Develop a program that allows the user to convert temperatures between Celsius and
# Fahrenheit.
#  Provide options for the user to choose the conversion direction (Celsius to Fahrenheit or
# vice versa) and enter the temperature value.
print('\t\t\t Temperature Converter ')
print('A : Celsius to Fahrenheit')
print('B : Fahrenheit to Celsius')
op = input('Choose A or B: ').upper()
con = int(input('Enter temperature: '))

if op == 'A':
    fahrenheit = con * 9/5 + 32
    print(f'Temperature in Fahrenheit is {fahrenheit}')
elif op == 'B':
    celsius = (con - 32) * 5/9
    print(f'Temperature in Celsius is {celsius}')
else:
    print('Invalid option')
