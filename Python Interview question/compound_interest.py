def compound_interest(p,t,r):
    amount=p*(pow(1+(r/100),t))
    return round(amount-p,2)
   
p=float(input("please enter principle amount: "))
t=float(input("please enter time: "))
r=float(input("please enter rate of interest: "))

print("the compound interest is",compound_interest(p,t,r))