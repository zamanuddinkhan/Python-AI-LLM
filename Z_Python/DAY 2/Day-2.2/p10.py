#Find the second largest element of list

lst = [1,2,3,4,89,99]
m = max(lst)
r = lst[0]
for i in lst:
    if i > r and i != m:
        r = i

print(r)        