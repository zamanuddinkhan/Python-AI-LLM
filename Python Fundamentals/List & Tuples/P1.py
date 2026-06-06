# Write a program to ask the user to enter names of their 3 favorite movies and store them in a list.

movie1 = input("Enter Favorite 1st Movie Name: ")
movie2 = input("Enter Favorite 2nd Movie Name: ")
movie3 = input("Enter Favorite 3rd Movie Name: ")

movies = [movie1, movie2, movie3]

print("Favorite Movies:", movies)

# OR

movies = []

movies.append(input("\nEnter Favorite 1st Movie Name: "))
movies.append(input("Enter Favorite 2nd Movie Name: "))
movies.append(input("Enter Favorite 3rd Movie Name: "))

print("Favorite Movies: ", movies)