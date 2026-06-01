try:
    a=int(input("enter a number: "))
    b=int(input("enter a number: "))
    print(a/b)
except:
    print("error!cannot divide by zero")    
finally:
    print("program finished ")   