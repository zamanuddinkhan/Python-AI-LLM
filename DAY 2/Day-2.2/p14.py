# find prime number in list -> greater than 1 and has two factors(1, itself)

lst = [0,1,2,3,4,5,6,7]
lst1 = [0,1,2,3,4,5,6,7]

for i in lst:
    if i == 2 or i == 3:
        print(i)
    if i % 2 != 0 and i % 3 != 0:
        print(i)

for n in lst1:
    for i in range(2,n):
        if n % i != 0:
            count = count + 1

