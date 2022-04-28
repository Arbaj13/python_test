
# 1,1,2,3,5,8
# def generate_fibonacci(n):
#     num1=0
#     num2=1
#     print(num1)
#     print(num2)
#     temp=0
#     for i in range(2,n):
#         temp=num1+num2
#         num1=num2
#         num2=temp
#         print(temp)  

# generate_fibonacci(8)



def fib(i):
    if i==0:
        return 0
    elif i==1:
        return 1    
    else:
        return (fib(i-2)+fib(i-1)  )  

index=int(input("enter here: "))
for i in range(index):
    if index<=0:
        print("please enter valid number")

    else:
        print(fib(i))