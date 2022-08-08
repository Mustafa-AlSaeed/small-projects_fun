year = int(input("Enter a year, to chheck if it is a leap year"))

if (year%400==0) and (year%100==0):
    print("the year {0} is a leap year".format(year))

elif year%4 ==0 and year%100 != 0:
    print("the year {0} is a leap year:".format(year))
else:
    print("this is not a leap year")
    
