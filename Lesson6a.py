
# A function -  is a block of statements performing specific task,
# a function is callable.
# 1. Functions split a large/big code in small chunks
# 2. One function can be called/accessed/invoked/reference more than once.

def welcome():
    print('Welcome to My Function')
    print('Thank you')
    #welcome()


def converter():
    dollars = 5000.7
    print("You have USD ", dollars)
    #print(type(dollars))
    shillings = dollars * 121.96
    print('You now have KES ',shillings)
    if shillings > 100000:
        print('Pay Tax')
    else:
        print('No Tax')



# # Call/Invoke
# converter()
# converter()
# welcome()


