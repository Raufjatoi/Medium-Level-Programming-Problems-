# 7. Temperature Converter:
#  Develop a program that allows the user to convert temperatures between Celsius and
# Fahrenheit.
#  Provide options for the user to choose the conversion direction (Celsius to Fahrenheit or
# vice versa) and enter the temperature value.
print('\t\t\t Tempertature Converter ')
print('A : celcius to fahren')
print('B : fahren to cel ')
op = input('Chose A and B : ').upper()
con = int(input('Enter temp : '))
if op == 'A':
    print(f'Temp in fahren is {con + 271}')
elif op == 'B':
    print(f'Temp in cel is {con - 271}')
else:
    print('invalid option')