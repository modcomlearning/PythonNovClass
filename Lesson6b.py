# Functions can have parameters
# below dollars/rate its parameter, its unknown
def converter2(dollars, rate):
    shillings = dollars * rate
    print('You had USD ', dollars)
    print('You now have ', shillings)
    print('Thank you')
    if shillings > 100000:
        print('Pay Tax')
    else:
        print('No Tax')


# provide arguments to fit the params
# converter2(dollars=2000, rate=119.5)
# converter2(dollars=1000, rate=121.5)
# converter2(dollars=float(input('How many dollars?')),
#            rate=float(input('What is the rate?')))

