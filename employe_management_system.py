class employee:
    def __init__(self,employee_id,name,department,salary):
        self.employee_id=employee_id
        self.name=name
        self.department=department
        self.salary=salary
    def employe(self):
        print("===== Employee Management system =====")
        print("Employe Id: ",self.employee_id)
        print("Name: ",self.name)
        print("Depatament: ", self.department)
        print("Salary: ",self.salary)
        if self.salary > 50000:
            print("Senior employe")
        else:
            print("Junior employe")
    def incriment(self,incriment):
        finaal_price=self.salary+incriment
        print("After incriment : ",finaal_price)

        
E1=employee("234rth33","Ram","Data entry",30000)
E2=employee("7657256ff","Sriram","Manager",100000)
E1.employe()
E1.incriment(200)
E2.employe()
E2.incriment(600)