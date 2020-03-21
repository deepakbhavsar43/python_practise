"""

"""

class Arithmetic:

    def __init__(self):
        self. value1 = 0.0
        self.Value2 = 0.0
        self.result = 0.0

    def Accept(self):
        self.value1= int(input("Enter value1 : "))
        self.value2= int(input("Enter value2 : "))

    def Addition(self):
        self.result = self.value1+self.value2
        return self.result

    def Subtraction(self):
        self.result = self.value1-self.value2
        return self.result

    def Multiplication(self):
        self.result = self.value1*self.value2
        return self.result

    def Division(self):
        self.result = self.value1//self.value2
        return self.result

if __name__ == "__main__":
    obj1 = Arithmetic()
    obj2 = Arithmetic()
    obj3 = Arithmetic()
    obj4 = Arithmetic()
    obj1.Accept()
    print(f"ADDITION\n{obj1.Addition()}")
    obj2.Accept()
    print(obj2.Subtraction())
    obj3.Accept()
    print(obj3.Multiplication())
    obj4.Accept()
    print(obj4.Division())