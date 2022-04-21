# TODO: Swapping of two number without  using temp

def swap(num1,num2):
    if num1<num2:
        print("if block-Before swap",num1,num2)
        num2=num1+num2
        num1=num2-num1
        num2=num2-num1
        print("if block-After swap",num1,num2)

    else:
        print("else block",num1,num2)
        num1=num1+num2
        num2=num1-num2
        num1=num1-num2

        print("else block after swap", num1,num2)

num1=int(input("Please enter you number : "))
num2=int(input("Please enter you number : "))

swap(num1,num2)