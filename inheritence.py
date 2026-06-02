class student:
    def study(self):
        print("i study")
class MLstudent(student):
    def code(self):
        print("i will code")
s1=MLstudent
s1.study(student)
s1.code(student)                