class employee:
    language = "Python"
    role = "developer"
    salary = 12000

    def getInfo(self):
        print(f"He is {self.language} {self.role} and has a {self.salary} salary")

ammar = employee()
ammar.getInfo()
# employee.getInfo(ammar)