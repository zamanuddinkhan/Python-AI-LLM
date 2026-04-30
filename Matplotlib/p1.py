import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y = x**2

# print(type(x))

# plt.plot(x, y)
# plt.plot(x, y, marker = 'o')
plt.plot(x, y, marker = 'o', linestyle = '--')


plt.title("Square Function Line Plot")
plt.xlabel('N value')
plt.ylabel('Square of N')

plt.show()