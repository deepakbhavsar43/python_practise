li=['a', 'b', 'c', 'd', 'e']
li_rm=['d','e']
print(li)
print(li_rm)
for i in li_rm:
    li.remove(i)
    print(li)
    print(li_rm)