# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 9}
# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)
c = A.symmetric_difference(B)
print(c)