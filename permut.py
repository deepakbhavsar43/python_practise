def permut(ss):
	x=10**(len(ss)-1)
	y=10**len(ss)
	lis=[]
	for i in range(1,len(ss)+1):
		lis.append(str(i))
	for i in range(x,y):
		sbuff=str(i)
		flag=0
		count=len(ss)
		for j in sbuff:
			if j in lis:
				count-=1
				lis.remove(j)
		lis=[]
		for i in range(1,len(ss)+1):
			lis.append(str(i))
		if count==0:
			for k in sbuff:
				print(ss[int(k)-1],end=' ')
			print()
		count=len(ss)

strr=input("Enter a string")
permut(strr)