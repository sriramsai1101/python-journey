num1=int(input("enter a number: "))
num2=int(input("enter a number: "))

operation=input("enter a operation: + ,-, / ,* = ")
if operation=="+":
    print(num1+num2)
elif operation=="-" :
    print(num1-num2)
elif operation=="*":
    print(num1*num2)
elif operation=="/":
    print(num1/num2)
else:
    print("invalid ")