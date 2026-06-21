# Que:4 WAF to print the elements of a list in a single line. (List is the parameter)

ls = [10, "zaman", 141, "uddin", 5, "khan"]

def print_ls(l):
    for item in l:
        print(item, end=" ")

print_ls(ls)