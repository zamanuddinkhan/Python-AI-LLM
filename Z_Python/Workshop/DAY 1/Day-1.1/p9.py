#chained comparisons, all parts must be true for the whole expression to be true.
#The moment one comparison fails → the entire chain becomes False.

print(34>45>56>67>78>89>90>444<333) # (34 > 45) and (45 > 56) and (56 > 67) and (67 > 78) and (78 > 89) and (89 > 90) and (90 > 444) and (444 < 333)

print(34>45>56>67>78>89>90>444) # (34 > 45) and (45 > 56) and (56 > 67) and (67 > 78) and (78 > 89) and (89 > 90) and (90 > 444)

print(34>2<1>0) #(34 > 2) and (2 < 1) and (1 > 0)

print(34>2>1) #(34 > 2) and (2 > 1)

print(2==3>1) #(2 == 3) and (3 > 1)

print(2==2>1) #(2 == 2) and (3 > 1)

print((34 > 45) and (45 > 56) and (56 > 67) and (67 > 78) and (78 > 89) and (89 > 90) and (90 > 444) and (444 < 333))

#comparison in strings (Python compares strings lexicographically, meaning character by character using their Unicode (ASCII) values.)
print('Amit'=="Amit")

print('Amit'>"Amit")
print('Amita'>"Amit")
