

def Fibonacci(i):
        if i==0:
            return 0
        elif i==1:
           return 1

        else:
            return Fibonacci(i-2)+Fibonacci(i-1)   



index=int(input("please enter your number: "))

if index <=0:
    print("please enter positive values")
else:
    for i  in range(index):
        print(Fibonacci(i))



