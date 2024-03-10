#4. Shopping Cart:
#  Simulate a basic shopping cart program.
#  Allow the user to add items (e.g., product name, price) to the cart.
#  Provide options to remove items and view the total cost of the cart
def main():
    print('\t\t\t Shoping Cart 🛒 ')
    d = {} 
    name = input('Enter name of item u wanna add : ').title()
    if name in d:
        print('item already exist')
        pass
    else:
     price = int(input(f'Enter the price of {name} : '))
     d[name] = price
    print(d)
    print('Wha ya wanna do now ? remove or wanna view the total cost : ')
    ans = input('Enter : ').lower()
    if ans in ['remo','r','remove']:
       r = input('Wha ya wanna remove').title()
       del d[r]
       print(d)
    elif ans in ['view','v','view total cost']:
      print(d)
    '''
    def remove():
       global ans
       global d
       r = input('Enter wha ya wanna remove : ')
       if r in d:
          del d[r]
          print('sucessfuly remove ', r)
       elif r  not in d:
          print('Cant find the item')
          pass
    def view():
        global d
        print(d)
        print(d)'''
main()   