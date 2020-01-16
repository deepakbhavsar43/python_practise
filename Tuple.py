# Empty tuple
my_tuple = ()
print(my_tuple) #output: ()
# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple) #output: (1, 2, 3)
# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple) #output: (1, 'Hello', 3.4)
# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple) #putput: ('mouse', [8, 4, 6], (1, 2, 3))
#tuple without using parenthesis
my_tuple = 1, 2, 3, "Deepak", "Bhavsar"
print(my_tuple) #output: (1, 2, 3, 'Deepak', 'Bhavsar')
a,b,c,d,e = my_tuple
print(a) #output: 1
print(b) #output: 2
print(c) #output: 3
print(d) #output: Deepak
print(e) #output: Bhavsar
#We will need a trailing comma to indicate that it is a tuple. 
my_tuple = "Deepak"
print(type(my_tuple)) #output: <class 'str'>
my_tuple = "Deepak",
print(type(my_tuple)) #output: <class 'tuple'>
#Access specific element using index
my_tuple = "Deepak",[1,2,3],['a','b','c']
print(my_tuple[1]) #output: [1, 2, 3]
print(my_tuple[2][1]) #output: b
#The index of -1 refers to the last item, -2 to the second last item and so on.
print(my_tuple[-1]) #output: ['a', 'b', 'c']
#slicing to access specific range of elements
print(my_tuple[1:3]) #output: ([1, 2, 3], ['a', 'b', 'c'])
#concate two tuples
print(my_tuple + my_tuple) #output: ('Deepak', [1, 2, 3], ['a', 'b', 'c'], 'Deepak', [1, 2, 3], ['a', 'b', 'c'])
#as tuple is immutable value cannot be changed
print('\n') # goes to new line
my_tuple[1] = 'Bhavsar'