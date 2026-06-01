class student:
    def __init__(self,name,college,branch,year):
        self.name=name
        self.college=college
        self.branch=branch
        self.year=year
    def introduce(self):
        print("my name is : ",self.name)
        print("my college: ",self.college)
        print("iam from: ",self.branch)
        print("from: ",self.year)
student1=student("sriram","avanthi","ai&ml","3rd year")
student2=student("eshwar","vivekanadha","degree","3rd year")
student3=student("rakesh","DRK","csm","3rd year")
student1.introduce()
student2.introduce()
student3.introduce()