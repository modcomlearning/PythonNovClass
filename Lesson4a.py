
# Program to Find the Largest of 3 numbers given
num1 = int(input("Enter your number1: "))
num2 = int(input("Enter your number2: "))
num3 = int(input("Enter your number3: "))

# Comparison, Logical
if num1 > num2 and num1 > num3:
    print('Number 1 is the Largest', num1)

elif num2 > num1 and num2 > num3:
    print('Number2 is the Largest', num2)

elif num3 > num1 and num3 > num2:
    print('Number 3 is the Largest', num3)

else:
    print('They are Equal')



