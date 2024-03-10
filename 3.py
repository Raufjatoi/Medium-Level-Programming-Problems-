# 3. Movie Recommendation System:
#  Design a program that asks the user for their favorite movie genre (e.g., comedy, action,
# drama).
#  Based on the user's input, recommend a few movies from that genre using a list of predefined movie titles and genres


# askin the user
comedy = ['Hera phary','Golmal','The mask','Mr bean','The boys']
drama = ['just watch pakistani dramas idk there names but they are best drama baz','prisners']
action = ['John Wick','300','Transformers']
entertainment = ['the wimplish','three idiots']
sci_fi = ['dark','back to future','ST(stranger things)','Umbrella academy']

print('Enter ya fav genra like : \n comedy , action ')
ans = input('Reply : ').lower()
if ans in 'comedy':
    for c in comedy:
        print(c,end=', ')
elif ans in 'action':
    for a in action:
        print(a,end=', ')
elif ans in 'sci-fic':
    for s in sci_fi:
        print(s,end=', ')
else:
    for e in entertainment:
        print(e,end=', ')
