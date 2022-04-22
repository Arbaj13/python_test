from more_itertools import first
from sympy import isprime


def isPrimeIn(first,second):
    for i in range(first,second+1):
        for j in range(2,i):
            if i%j==0:
                # print("not a prime")
                break
        else:
            print(i,"it is a prime number")

firstnum=int(input("pleaase enter a first interval:"))

secondnum=int(input("pleaase enter a second interval:"))

if (firstnum<secondnum) and (firstnum>1 and secondnum>2):
    isPrimeIn(firstnum,secondnum)

else:
    print("please enter a valid value")

           