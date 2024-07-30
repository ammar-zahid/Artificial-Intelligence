class employee:
    name = 'ammar'
    language = "Python"
    salary = 12000

    @staticmethod
    def greet(): #this function doesnt need argument 
        print("Good Morning")

    def __init__(self, name, language, salary): #dunder method which is automatically called
        self.name = name
        self.language = language
        self.salary = salary

        print(f"{self.name, self.language, self.salary}")

ammar = employee("ammar", "JS", 1111)
# ammar.getInfo()
# ammar.greet()
# employee.getInfo(ammar)