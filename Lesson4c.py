
# Nested Conditional
points = int(input('Your Points: '))
age = int(input('Your Age: '))

if points < 50:
    print('Not Considered for A TRIP')

elif points >= 50 and points < 75:
    print('We will consider a Prize')

else:
    print('We Consider A TRIP')
    if age < 10:
        print('Will take to Kids Place')
    else:
        print('Educational TRIP')


