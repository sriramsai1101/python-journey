class library:
    def __init__(self,book_name,author,total_books):
        self.book_name=book_name
        self.author=author
        self.total_books=total_books
    def display(self):
        print("=====LIBRARY=====")
        print("BOOK_NAME: ",self.book_name)
        print("AUTHOR: ",self.author)
        print("Total_Books",self.total_books)
    def borrow(self,borrow):
        print("taken books :",borrow)
        self.total_books=self.total_books-borrow
        print("Remaining books: ",self.total_books)
    def return_books(self,return_books):
        print("return books",return_books)
        return_books=self.total_books+return_books
        print("Total books in library: ",return_books)
        
          
        
        
b1=library("python","gudio",9)
b1.display()
b1.borrow(5)
b1.return_books(3)
        

        


        
        



         
            
              