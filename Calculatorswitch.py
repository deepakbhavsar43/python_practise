def addition(num1, num2):
    num1 += num2
    return num1


def subtraction(num1, num2):
    num1 -= num2
    return num1


def mul(num1, num2):
    num1 *= num2
    return num1


def division(num1, num2):
    num1 /= num2
    return num1


def module(num1, num2):
    num1 %= num2
    return num1


def default(num1, num2):
    return "Incorrect day"


switcher = {
    1: addition,
    2: subtraction,
    3: mul,
    4: division,
    5: module
}


def switch(operation):
    return switcher.get(operation, default)(num1,num2)


operation = int(input("Enter number of the operation you want to perform:"))
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print(switch(operation))
