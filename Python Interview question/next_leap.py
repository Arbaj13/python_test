# from operator import ne


# def next_leap(year):
#     n=15
#     while n!=0:
#         if (year % 400 == 0) and (year % 100 == 0):
#             print(f"The next leap year from {year} is {year + 4}")
#             year+=4
                    
#         elif (year % 4 ==0) and (year % 100 != 0):
#             print(f"The next leap year from {year} is {year + 4}")          
#             year+=4

#         while not next_leap(year):
#             year+=1
#             next_leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 ==0
#             print(f"The next leap year from {in_year} is {year}")
#         n-=1
# in_year=int(input('ENTER '))
# next_leap(in_year)
    

def next_leap(year,n):
    while n!=-1:
        leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 ==0
        if leap:
            print(f"The next leap year is {year}")
            year+=4
        else:    
            while not leap:
                year += 1
                leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 ==0
            # print(f"The next leap year is not {year}")      
        n-=1

inp_year = int(input("Give year:"))
n=int(input("Please enter number of iterations :"))
next_leap(inp_year,n)   



