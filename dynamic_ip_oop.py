class seq:

    def val(self, n):
        self.n=n
        user_input=[]
        for i in range(0,n):
            temp=int(input("Enter integer %: ",i))
            user_input.append(temp)

n=input("Enter total number of integers : ")
obj =seq(n)
