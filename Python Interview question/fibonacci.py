# TODO: print  Fibonachi series


def Fibonachi(index):
    firstnumber=0
    secondnumber=1
    temp=0
    print(firstnumber)
    print(secondnumber)
    for i in  range(index-2):
        temp=firstnumber+secondnumber
        firstnumber=secondnumber
        secondnumber=temp
    
        print(temp)


index=int(input("please enter your number: "))
Fibonachi(index)