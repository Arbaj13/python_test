def concat(param):
    result=''
    for i in range(1,param+1):
        result=result+str(i)
    print (result)

num=int(input("please enter your value here :"))
if num>0:
    concat(num)
else:
    print("invalid digit")    