import matplotlib.pyplot as plt

heroes = ['Prabhas', 'Pawan', 'Ceeranjeevi', 'Sharukh', 'Amitabh'] #x-axis values
movies = [100,300,200,600, 1000] #Height of bars, values for y axis

c = ['r', 'b', 'k', 'g', 'orange']

# plt.bar(heroes, movies)
plt.bar(heroes, movies, color = c) # in different colors

plt.xlabel('Hero Name', color = 'b', fontsize = 15)
plt.ylabel('Number of movies', color = 'b', fontsize = 15)
plt.title('Hero wise number of movies', color = 'r', fontsize = 15)

plt.show()