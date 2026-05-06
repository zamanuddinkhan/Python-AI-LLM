#Keyword Arguments

def data(name,add,mob,un,pw):
    print("Details: ")
    print("Name = ",name)
    print("Address = ",add)
    print("Mobile No. = ",mob)
    print("Username = ",un)
    print("Password = ",pw)

data("Srishti","Indore",8889,"SD",12345) #positional
data(name = "Tinka",add = "Ujjain",mob = 2234, pw = 12, un = "twinkle") #keword 
data(add = "Delhi",mob = 1190,name = "Tiku", pw = 12, un = "twinkle")
data(pw = 122, un = "puuung",name = "Shahjada",add = "India",mob = 21234)