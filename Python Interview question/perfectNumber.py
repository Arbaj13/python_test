
def perfectNum(num):
    sum=0
    for i in range(1,(num//2)+1):
        if num%i==0:
            sum=sum+i  

    return sum
    
num=int(input("please enter a number :"))
sum=perfectNum(num)
if sum==num:    
    print("This number is Perfect number ")
else:
    print("not a perfect number") 



   