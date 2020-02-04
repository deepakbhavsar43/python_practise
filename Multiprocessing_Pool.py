import time
from multiprocessing import Pool


def sum_square(number):
    s=0 
    for i in range(number):
        print(f"in for {i}")
        s+=i*i
        print(f"sum is {s}")
    return s

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    p = Pool()
    result = p.map(sum_square, numbers)
    print(result)
    p.close()
    p.join()