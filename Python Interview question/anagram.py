from numpy import angle
from sqlalchemy import false, true


def anagram(str1,str2):
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False    


str1=str(input("please enter a string: "))

str2=str(input("please enter a string: "))

str3=sorted(str1)
print(str3)

if anagram(str1,str2):
    print("it is a anagram")
else:
    print("not a anagram")    