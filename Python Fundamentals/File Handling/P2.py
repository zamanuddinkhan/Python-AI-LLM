# WAF to find in which line of the file does the word "learning" occur first. Print -1 if word not found.
def check_for_line():
    word = "Learning"
    data = True
    line_no = 1
    f = open("Python Fundamentals\File Handling\practice.txt", "r")
    while data:
        data = f.readline()
        if word in data:
            f.close()
            return line_no

        line_no += 1
    f.close()
    return -1

print(check_for_line())