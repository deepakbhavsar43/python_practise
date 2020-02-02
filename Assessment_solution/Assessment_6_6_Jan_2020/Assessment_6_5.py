"""Accept file name and one string from user and return the frequency of that string from file.
Input: Demo.txt Marvellous
Search “Marvellous” in Demo.txt"""


def read_lines(f):
    print(f)
    count = 0
    read_f1 = []
    with open(f[0], "r", encoding="UTF-8") as file1:
        for l in file1:
            # print(f"Reading from file : {l}")
            read_f1.append(l.split(" "))
            # This will find the Marvellous as substring in each and every string
            # print(l.find(f[1]))
            print(l)
            # if (l.find(f[1])==-1):
            #     pass
            #     # print()
            # else:
            #     # print("In if condition")
            #     count += 1

        print(read_f1)

    # This code does not work because at the end of string  "\n" new line symbol is added. for ex :- "Marvellous\n"
    # if f[1] in read_f1:
    #     for i in read_f1:
    #         print(f"in i {i}")
    #         print(f"in i {f[1]}")
    #         if i == f[1]:
    #             count = count + 1
    # else:
    #     print(f"Given string not in {f[0]}")

    return count


if __name__ == "__main__":
    # count = 0
    # f_name = input("Enter the file name : ")
    # files = f_name.split(" ")
    files = ['Demo.txt', 'Marvellous']
    result = read_lines(files)
    print(result)
    # print(f"The frequency of {files[1]} in file {files[0]} is {result}.")
