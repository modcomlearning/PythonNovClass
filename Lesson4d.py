
year = int(input('Enter Year: '))
if year%4 == 0:
    print('It might be A Leap Year')
    if year%4==0 and year%100 != 0:
        print('Its A Leap year')

    else:
        print('Its Might be a leap year')
        if year%4 ==0 and year%100==0 and year%400==0:
            print('Its A Leap Year')
        else:
            print('Its Not A Leap Year')
else:
    print('Its Not A Leap Year')




