# BMI calculator
def bmi(weight, height):
    answer = weight / (height * height)
    print('BMI ', answer)
    if answer < 17.5:
        print('Underweight')

# reference
bmi(weight=78.7, height=3)

