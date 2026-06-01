#class is an blueprint
class student:
    def __init__(self,name,college):
        self.name=name
        self.college=college
    def introduce(self):
        print("my name is " ,self.name)
        print("my college id : ",self.college)
student1=student("sriram","avanthi")
student2=student("eshwar","jntuh")
student1.introduce()       

student2.introduce()