import matplotlib.pyplot as plt
import numpy as np

marks = np.array([25, 30, 43, 12])

mylabels = ['Python', 'Java', 'Devops', 'DataScience']
myexplode = [0.0, 0.0, 0.0, 0.2]

plt.pie(marks, labels=mylabels, autopct='%.2f%%', explode=myexplode)

plt.show()