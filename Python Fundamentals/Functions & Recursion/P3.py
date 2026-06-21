# Que:3.1 Write a function that takes a list as a parameter and prints the largest number in it.

ls = [0, 6, 8, 15, 100, 55, 40, 7, 3, 22, 76]

def lar_num(l):
    print("Maximun Number: ",max(l))

lar_num(ls)

# Que:3.2 Write a function that takes a list as a parameter and prints the smallest number in it.

tp = (0, 6, 8, 15, 100, 55, 40, 7, 3, 22, 76)

def sml_num(t):
    print("Minimum Number: ",min(t))

sml_num(tp)

# Que:3.3 Write a function that takes a set of numbers and prints the sum of all elements.

st = {0, 6, 8, 15, 100, 55, 40, 7, 3, 22, 76}

def sum_num(s):
    print("Sum: ",sum(s))

sum_num(st)

# Que: 3.4 Write a function that takes a list and prints how many even numbers are present.

num = [0, 6, 8, 15, 100, 55, 40, 7, 3, 22, 76]

def even_detect(e):
    count = 0
    for num in e:
        if num % 2 == 0 :
            count += 1
    print("Count of Even Numbers:", count)

even_detect(num)

# Que:3.5 Write a function that takes a tuple and prints the square of each element.

no = (0,1,2,3,4,5,6,7,8,9,10)

def square(s):
    for num in s:
        result = num * num
        print("Square of", num, "is", result)

square(no)