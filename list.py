# Creating a List with 
# mixed type of values 
# (Having numbers and strings) 
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks'] 
print("\nList with the use of Mixed Values: ") 
print(List) 
#adding element to existing list
List.append('Deepak')
print(List)
#adding element at desired position
List.insert(3,3)
print(List)
List.extend(['Arun','Bhavsar',7])
print(List)
#print the last element of the list (Negative indexing)
print(List[-1])
#remove element from list
List.pop(1)
print(List)
#by default pops last element
List.pop()
print(List)
#slicing method to print specific range from list
print(List[7:10])

