from operator import le


def length_of_string(x):
    len_count=0
    for i in x:
        len_count=len_count+1
    
    print(len_count)
#Driver code
x=input("please enter your string here: ")
length_of_string(x)

print(len("hello world i am arbaj"))