def reverse_string(x):
    reverseString= ""
    for i in x:
        reverseString=i+reverseString
    print(reverseString)


#driver code
x=input("please enter here : ")
reverse_string(x)


