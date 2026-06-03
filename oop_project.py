class bank:
    def __init__(self):
        self.__balance=50000
    def show_balance(self):
        print("balance:",self.__balance)
    def deposit(self,amount):
        
        print("deposited: ",amount)
        print("current balance: ",amount+self.__balance)
        self.__balance = self.__balance + amount

    def withdraw(self,cash):
        if cash<self.__balance:
          print("withdral: ",cash)
          print("current balance: ",self.__balance-cash)
          self.__balance = self.__balance - cash 

        else:
         print("your cant withdraw that ammount becauseyour current balance is : ",self.__balance)    
        
s=bank()
s.show_balance()
s.deposit(1000)
s.withdraw(600000)
                
       

