def reverseNum(num):
    rev=0
    while num!=0:
        rev=(rev*10)+(num%10)
        num=num//10
    return rev


num=int(input("please enter a number :"))
 
print("The reversed number is :",reverseNum(num))
