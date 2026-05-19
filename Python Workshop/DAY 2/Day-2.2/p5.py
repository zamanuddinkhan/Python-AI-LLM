#List as Queue

from collections import deque

queue = deque(["tinka","tiku","sonu","puung"])
print(queue)

queue.append("motu")
print(queue)

print(queue.popleft())
print(queue)
