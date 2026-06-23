# Que:8 Write a recursive function to print all elements in a list.
# Hint: Use list & index as parameters

def print_list(ls, idx = 0):
    if(idx == len(ls)):
        return
    print(ls[idx])
    print_list(ls, idx + 1)

lst = ["a","b","c","d"]
print("Elements of List are: ")
print_list(lst)