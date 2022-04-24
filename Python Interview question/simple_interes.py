def simpleInterest(p,t,r):
    print("the principle is",p)
    print("the principle is",r)
    print("the principle is",t)

    return (p*t*r)/100



p=int(input("please enter principle amount: "))
t=int(input("please enter time: "))
r=int(input("please enter rate of interest: "))

print("the simple interest is",simpleInterest(p,t,r))
