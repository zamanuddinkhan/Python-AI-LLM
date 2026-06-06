str = "I am a Coder."

str.endswith("er.")
print(str.endswith("er."))

str.capitalize()
print(str.capitalize())

str.replace("a", "A")
print(str.replace("a", "A"))

str.find("Coder")
print(str.find("Coder"))

str.count("a")
print(str.count("a"))

str.startswith("I am")
print(str.startswith("I am"))

str.lower()
print(str.lower())

str.upper()
print(str.upper())

str.title() # each word's first letter will be capitalized
print(str.title())

str.swapcase()
print(str.swapcase())

str.strip() # removes spaces from start and end of the string, not from the middle.
print(str.strip())

str.lstrip() # removes spaces from the start of the string, not from the end and middle.
print(str.lstrip())

str.rstrip() # removes spaces from the end of the string, not from the start and middle.
print(str.rstrip())

str.split() # splits the string into a list of words using space as default separator.
print(str.split())

str.split("a") # splits the string into a list of words using "a" as separator, "a" will not be included in the result.
print(str.split("a"))

str.split(" ", 2) # splits the string into a list of words using space as separator, but only splits at the first 2 occurrences of the separator, so the result will be a list with 3 elements.
print(str.split(" ", 2))

str.splitlines() # splits the string into a list of lines using newline character as separator, newline character will not be included in the result.
print(str.splitlines())

str.partition("a")
print(str.partition("a"))

str.rpartition("a")
print(str.rpartition("a"))

str.rfind("C")
print(str.rfind("C"))

str.index("Coder")
print(str.index("Coder"))

str.rindex("a")
print(str.rindex("a"))

str.isalpha() 
print(str.isalpha())

str.isalnum() 
print(str.isalnum())

str.islower()
print(str.islower())

str.isupper()
print(str.isupper())

str.isspace()
print(str.isspace())

str.isprintable() 
print(str.isprintable())

str.isidentifier() 
print(str.isidentifier())

str.isnumeric()
print(str.isnumeric())

str.isdecimal()
print(str.isdecimal())

str.isdigit()
print(str.isdigit())

str.casefold() 
print(str.casefold())

str.encode() 
print(str.encode())

str.expandtabs()
print(str.expandtabs())

str.join(["I", "am", "a", "Coder."])
print(str.join(["I", "am", "a", "Coder."]))

str.maketrans("a", "A")
print(str.maketrans("a", "A"))

str.zfill(20)
print(str.zfill(20))

str.center(30)
print(str.center(30))

str.removeprefix("I am ")
print(str.removeprefix("I am "))

str.removesuffix("er.")
print(str.removesuffix("er."))

str.isascii()
print(str.isascii())

str.center(30, '*')     # with fill character
print(str.center(30, '*'))

str.ljust(30)
print(str.ljust(30))

str.rjust(30)
print(str.rjust(30))

s = "Hello {}"
print(s.format("Zaman"))