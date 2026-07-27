class book:
    def __init__(self,title,author,price,quantity):

        self.title=title
        self.price=price
        self.author=author
        self.quantity=quantity
    def display(self):
        print("========BOOK DETAILS========")
        print("Book name : ",self.title)
        print("Price : ",self.price)
        print("Author : " ,self.author)
        print("Remaing books : ",  self.quantity)
        if self.quantity>0:
            print("availabe")
        else :
            print("out of stock ")
        
    def discount(self,percent):
        final_price =self.price-(self.price*percent/100)
        print("=====Discounts for books======")
        print("discounted price: ", final_price)
b1=book("python","gudio",2300,2)     
b2=book("AI basics","andrew",750,0)
b1.display()
b2.display()
b1.discount(10)
b2.discount(20)