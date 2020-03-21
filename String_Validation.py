if __name__ == '__main__':
    s = input()
    # s='Deep123'
    li = list(s)
    ori_li = li.copy()
    int_li = []
    li_rm = []
    # alnum = s.isalnum()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False

    leng = len(li)

    for i in range(leng):
        re = li[i].isalpha()
        if re == False:
            temp = li[i]
            li[i] = int(temp)
            digit = True
            int_li = li.copy()
            li_rm.append(li[i])
            # li.remove(i)

    # print(f"input list {li}")
    # print(f"copy of input list {ori_li}")
    # print(f"list after type cast{int_li}")
    # print(f"list of ele to remove {li_rm}")

    for i in li_rm:
        li.remove(i)

    # print(li)

    for i in li:
        if i.isalpha() == True:
            alpha = True

        if i.isdigit()==True:
            digit=True

        if i.islower() == True:
            lower = True

        if i.isupper() == True:
            upper = True

        if alpha == True and digit == True:
            alnum=True

    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)