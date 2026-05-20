# Change the default width 

import matplotlib.pyplot as plt

heroes = ['Prabhas', 'Pawan', 'Ceeranjeevi', 'Sharukh', 'Amitabh']
movies = [100,300,200,600, 1000]

w = [0.3, 0.3, 0.3, 0.3, 0.6] # set the width

plt.bar(heroes, movies, width = w)

plt.xlabel('Hero Name', color = 'b', fontsize = 15)
plt.ylabel('Number of movies', color = 'b', fontsize = 15)
plt.title('Hero wise number of movies', color = 'r', fontsize = 15)

plt.show()