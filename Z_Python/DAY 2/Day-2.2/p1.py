'''
list is a collection of homogeneous objects
list is collection of different types of data types
list is mutable
list preseve order of insertion
'''
# lst = [10,20,30,40,50,'puuung', 'sonu', 666.777]

lst1 = [100,200,300,400]
lst2 = [1000,2000,3000]
lst = [10,20,30,40,50]
lst.append(lst1)

print(lst[5][2]) #prints 300

lst.extend(lst2)
print(lst)

copied = lst.copy()
print(copied)

firstindex = lst.index(10)
print(firstindex)

counted = lst.count(10)
print(counted)

lst.clear()
print(lst)