"""
Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000
"""
from functools import reduce

class fmr:
    # def __init__(self):
    # InList =  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70, 95]
    InList = []
    flag=1
    while flag == 1:
        num = input()
        if num == "done":
            flag = 0
        else:
            InList.append(int(num))

    print(f"Original list is : {InList}")
    
    def fmr(self):
        # result = reduce(lambda x, y: x*y, map(lambda x: x + 10, filter(lambda x: x<=90, filter(lambda x: x>=70, obj1.InList))))
        # print(f"Result is : {result}")
        filtered = list(filter(lambda x: x<=90, filter(lambda x: x>=70, obj1.InList)))
        print(f"List after filter  : {filtered}")
        mapped = list(map(lambda x: x + 10, filtered))
        print(f"List after map : {mapped}")
        reduced = reduce(lambda x,y: x*y, mapped)
        print(f"Output of reduced : {reduced}")


if __name__ == "__main__":
    obj1 =  fmr()
    obj1.fmr()

