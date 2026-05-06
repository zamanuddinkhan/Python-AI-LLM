"""A lambda function is an anonymous function (doesn’t need a name).
It is used for short and simple operations.
    arguments → input values
    expression → a single operation that is automatically returned

Rules / Points:-
1) Lambda can have only one expression (no multiple statements).
2) Result of lambda is automatically returned.
3) You can use print(), but it returns None.
4) Lambda is often used for temporary functions with map(), filter(), reduce(), sorted().
"""

#Normal function
def add(x,y):
    return x+y

print(add(3,5))


#lambda function -> lambda arguments: expression
add = lambda x,y : x+y

print(add(3,5))

nums = [1,2,3,4]

#square each number with lambda function + map()
squared = list(map(lambda x: x**2, nums))
print(squared)

#select only even with of lambda + filter()
even_nums = list(filter(lambda x: x%2==0,nums))
print(even_nums)