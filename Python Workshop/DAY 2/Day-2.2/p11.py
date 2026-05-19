#Find the second largest element of tuple

t = (1,2,3,4,89,89,99,99)

p = max(t)
r = t[0]
for i in t:
    if r < i and i != p:
        r = i
print(r)