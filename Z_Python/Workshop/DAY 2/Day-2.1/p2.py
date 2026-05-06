#Time Module

import time

current_time = (time.time())  #Returns the current time in seconds since January 1, 1970 (called the epoch)
print(current_time)

print("Hello")
time.sleep(5)
print("Srishti")


readable_time = time.ctime(current_time)
print(readable_time)

# time.localtime([seconds])
