line = "my college name is SAIT , SAIT is a student driven college. SAIT is in Indore"

# print(a.find("SAIT"))

word='SAIT'

i = line.find(word)

if i == -1:
    print("String is empty.")

while i != -1:
    print("{} present at {} position".format(word,i))
    i= line.find(word, i + len(word), len(line))