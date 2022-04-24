def occurance(mychar,mystring):
    count=0
    for i in range(len(mystring)):
        if mystring[i]==mychar:
            count=count+1
    return count


mychar=str(input("please a char :"))
mystring=str(input("please enter a string :"))

print(f"the char {mychar} is available in {mystring} ",occurance(mychar,mystring),"times")
