#Take a number as input and tell whether it is even or odd without using % , / , //

number = int(input("Enter a number: "))

# for i in range(0,100):
#     if number == 2*i:
#         print("Even")
#         exit()
#     else:
#         print("odd")
#         exit()

if number & 1:
    print("odd")
else:
    print("even")
