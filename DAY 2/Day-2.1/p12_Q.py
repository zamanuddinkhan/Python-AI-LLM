# To check type of characters present in a string
# isalnum() isalpha() isdigit()

'''
s = "a5b6c3d9"

#expected outcome: aaaaa bbbbbbccc ddddddddd
n= 5

for i in s:
    if(i == 'c'):
        n=3
    if i.isalpha():
        print(i*n,end="")
        n = n + 2
'''

# s = 'a5b6c7d3'

s = input("Enter format:")
cur,prev = '',''

for i in s:
    if i.isalpha():
        cur = cur+i
        prev = i
    elif i.isdigit():
        cur = cur+prev*(int(i)-1)

print(cur)