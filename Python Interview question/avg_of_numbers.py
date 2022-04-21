# TODO: To find average of numbers

def collectingNumbers(total_number):
    for i in range(total_number):
        num=int(input("please enter numbers here : "))
        mylist.append(num)


def avg():
    total=0
    for i in range(len(mylist)):
        total=total+mylist[i]
    return total//total_number   

mylist=[]
total_number=int(input("avg of how many numbers??` : "))

collectingNumbers(total_number)
avg=avg()
print(avg)


