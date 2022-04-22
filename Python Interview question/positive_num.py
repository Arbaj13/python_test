def ispositive(param):
    if param>0:
        print("The number is positive")
    elif param<0:
        print("the number is negative")  
    else:
        print("the number is zero")      

num=int(input("enter your number:"))        
ispositive(num)