"""
Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
Input List = [2, 70, 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
"""
from functools import reduce

class fmr:
    PrimeList, InList = [], []
    flag=1
    print("Enter elements in list : ")
    while flag==1:
        num = input()
        if num=="done":
            flag=0
        else:
            InList.append(int(num))
    # InList = [2, 4, 70, 11, 10, 17, 23, 31, 77]
    # InList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    print(f"Input List : {InList}")

    def mapping(self):
        mapped = list(map(lambda x: x*2, fmr.PrimeList))
        print(f"List after map : {mapped}")
        result =(reduce(lambda x,y: x if x>y else y, mapped))
        print(f"Maximum number in list : {result}")


    def prime(self):
        # filtered = list(filter(lambda x: (x%2==0, fmr1.InList))
        # print(f"List after filter : {filtered}")
        for i in fmr.InList:
            flag = 0
            if i == 2:
                fmr.PrimeList.append(i)
            elif i > 2:
                for j in range(2, i):
                    # print(f"in for loop value of i :{i} and j :{j}")
                    if j < i and i % j == 0:
                        # print(f"in if condition value of i :{i} and j :{j}")
                        # i%j==0
                        flag = 1
                        break
                        print("after break")
                if flag == 0:
                    fmr.PrimeList.append(i)
            flag = 0
        print(f"Prime list : {fmr.PrimeList}")
        # fmr.mapping(self,fmr.PrimeList)

        def mapping(self, li):
            mapped = list(map(lambda x: x*2, li))
            print(f"List after map : {mapped}")
            result =(reduce(lambda x,y: x if x>y else y, mapped))
            print(f"Maximum number in list : {result}")

        mapping(self, fmr.PrimeList)

if __name__ == "__main__":
    obj1 = fmr()
    obj1.prime()
    # obj1.mapping()
