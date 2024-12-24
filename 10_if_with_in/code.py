
movies_watched = {"Matrix", "Alien", "Box"}
user_movie  = input("Enter a movie your recently watched: ")

if user_movie in movies_watched:
    print(f"I have watched {user_movie} too")
else:
    print(f"I have not watched {user_movie}")


