word = "operations"
line = 1

with open("Python-AI-LLM\Python Fundamentals\Practice_Questions\simple.txt", "r") as f:
  
  while True:
    data = f.readline()
    if (word in data):
       print(f"{word} word found at line no {line}")
       break
    line += 1