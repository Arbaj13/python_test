def palindrom(num):
    rev=0
    while num!=0:
        rev=(rev*10)+(num%10)
        num=num//10
    return rev

num=int(input("please enter a number :"))
rev=palindrom(num)
if rev==num:
    print("the number provided is a palindrom number")   
else:
    print("the number provided is not a palindrom")    
