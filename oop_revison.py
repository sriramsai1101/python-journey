class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print(self.name)
        print(self.roll_no)
        print(self.marks)
        average=sum(self.marks) / len(self.marks)
        print(average)
        if average >= 90:
            print("A grade ")
        elif average>=75:
            print("B grade ")
        elif average >= 60:
            print("c grade")
        else:
            print("Fail")
        
s1=student("sriram","24pt1a6610",[19,20,13])
s2=student("ram","223344h44",[90,80,70])
s1.display()
s2.display()