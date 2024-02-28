import json
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
movielist = []
movies_file = open('movies.json')
movielist = json.load(movies_file) 
movies_file.close()
seen = "Unseen"
while True:
    print("1. Add a movie to watch ")
    print("2. Remove a movie ")
    print("3. Point a movie as watched ")
    print("4. Filter watched movies ")
    print("5. Filter unwatched movies ")
    print("6. Show top 10 movies by rating ")
    print("7. Clear up the movie list ")
    print("8. Search a movie ")
    print("e. Exit and save ")
    command = input("\nChoose command: ")
    if command == "1":
        while True:
            movie_name = input("Type name of the movie ")
            if len(movie_name) > 2 or len(movie_name) < 120:
                break
        movie_rating = int(input("Type its rating "))
        movies = {
            "Name" : movie_name,
            "Rating": movie_rating,
            "Seen": seen
        }
        movielist.append(movies)
        print (movielist)
    elif command == "2":
        movie_to_be_deleted = input("Type a name of movie you want to delete ")
        for i in range(len(movielist)):
            if movielist[i]['Name'] == movie_to_be_deleted:
                del movielist[i]
            else:
                print("Invalid name")
    elif command == "3":
        bufer = {}
        movie_to_be_pointed_as_seen = input("Type a name of movie you want to point as seen ")
        for i in range(len(movielist)):
            if movielist[i]['Name'] == movie_to_be_pointed_as_seen:
                bufer = movielist[i]
                bufer["Seen"] = "Seen"
                del movielist[i]
                movielist.append(bufer)
            else:
                print("Invalid name")
    elif command == "4":
        seen_movies_list = []
        for i in range(len(movielist)):
            if movielist[i]['Seen'] == "Seen":
                seen_movies_list.append(movielist[i])
        print (seen_movies_list)
    elif command == "5":
        unseen_movies_list = []
        for i in range(len(movielist)):
            if movielist[i]['Seen'] == "Unseen":
                unseen_movies_list.append(movielist[i])
        print (unseen_movies_list)
    elif command == "6":
        top_movies_list = []
        def sorted_top_10(movielist):
            return int(movielist["Rating"])
        top_movies_list = sorted(movielist, key = sorted_top_10, reverse = True)
        for x in top_movies_list[:10]:
            print(x)
    elif command == "7":
        movielist.clear()
    elif command == "8":
        searched_movie_list = []
        searched_movie = input("Type its name ")
        for i in range(len(movielist)):
            if searched_movie in movielist[i]['Name']:
                searched_movie_list.append(movielist[i])
        print (searched_movie_list)
    if command == "e":
        print("Exiting...")
        break
with open ("movies.json", "w") as file: 
    json.dump(movielist, file)
