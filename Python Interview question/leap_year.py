def leapYear(year):
    if ((year%400==0) | (year%100!=0) &(year%4==0)):
        print("It's leap year")
    else:
        print("not leap year")    


year=int(input("please enter year: "))
leapYear(year)
