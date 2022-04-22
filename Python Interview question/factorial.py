def factorial(num):
    result=1
    while num!=0:
        result=result*num
        num=num-1
    return result



num=int(input("please enter a number :"))
print("the factorial of ",num,"is ", factorial(num))