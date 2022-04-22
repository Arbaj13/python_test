def isPrime(param):
    for i in range(2,param):
        if param%i==0:
            print(param,"it's not a prime number")
            break
    else:
        print(param,"It's prime number")    

num=int(input("please enter a value here :"))

if num>1:
    isPrime(num)
else:
    print("enter a valid number")    
    