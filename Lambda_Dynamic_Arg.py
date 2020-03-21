# f = (lambda x: x+2)(nonlocal n)
if __name__ == "__main__":
	n = int(input("Enter a int : "))
# 	result = f()
# 	print(result)
	f = (lambda x: x+2)(n)
	print(f)