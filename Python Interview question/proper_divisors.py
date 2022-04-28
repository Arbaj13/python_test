def proper_devisor(num):
    list=[]
    for i in range(1,(num//2)+1):
        if num%i==0:
            list.append(i)
    print(f"proper diviors of {num} are",list)

num=int(input("please enter a number :"))
proper_devisor(num)
