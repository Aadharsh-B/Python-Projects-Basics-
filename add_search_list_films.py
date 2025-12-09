#List of Films
MOVIES_DB = [
    {
        "film_title": "inception",
        "release_year": "2010",
        "director": "christopher nolan"
    },
    {
        "film_title": "the shawshank redemption",
        "release_year": "1994",
        "director": "frank darabont"
    },
    {
        "film_title": "the godfather",
        "release_year": "1972",
        "director": "francis ford coppola"
    },
    {
        "film_title": "parasite",
        "release_year": "2019",
        "director": "bong joon-ho"
    },
    {
        "film_title": "pulp fiction",
        "release_year": "1994",
        "director": "quentin tarantino"
    },
    {
        "film_title": "the dark knight",
        "release_year": "2008",
        "director": "christopher nolan"
    },
    {
        "film_title": "spirited away",
        "release_year": "2001",
        "director": "hayao miyazaki"
    },
    {
        "film_title": "the matrix",
        "release_year": "1999",
        "director": "lana wachowski"
    },
    {
        "film_title": "mad max: fury road",
        "release_year": "2015",
        "director": "george miller"
    },
    {
        "film_title": "la la land",
        "release_year": "2016",
        "director": "damien chazelle"
    }
]

def quit_function():
    while True:
        check_flag = input("\nEnter 'y' to Stay on Page or 'n' to EXIT : ")
        if check_flag.lower() == 'y':
            return True
        elif check_flag.lower() == 'n':
            return False
        else:
            print("Invalid input. Enter 'y' [OR] 'n'.")

def add_movie():
    print("\nADD FILMS :")

    appended_film =     {
        "film_title": "",
        "release_year": "",
        "director": ""
    }

    appended_film["film_title"] = input("Enter Film Title : ")
    appended_film["release_year"] = input("Enter Release Year : ")
    appended_film["director"] = input("Enter Director : ")

    if appended_film in MOVIES_DB:
        return "FILM availabe in Data Base"
    else:
        MOVIES_DB.append(appended_film)

    print("FILM Added to Data Base! \n")

    # Print a List of Films
    list_movies()
    return ""

def list_movies():
        print("\nLIST OF FILMS \n")

        for movie in MOVIES_DB:
            # Quote Matching :)
            print(f"{movie['film_title'].title()} ({movie['release_year']}) - by {movie['director'].title()}")

        
        return "END of LIST"

def search_movie():
    print("\nSEARCH FILM")
    print("""
           Search by : 
           1. Film Title - Enter 'film_title'
           2. Release Year : XXXX - Enter 'release_year'
           3. Director - Enter 'director'\n
           """)
    
    search_by = input("ENTER SEARCH PARAMETER : ")

    if search_by not in ["film_title", "release_year", "director"]:
        print("Invalid search parameter!")
        return

    film_parameter = input(f"Enter the {search_by} : ")

    print ("\nSTART of LIST \n")

    for movie in MOVIES_DB:
        if movie[search_by] == film_parameter:
            print(f"{movie['film_title'].title()} ({movie['release_year']}) - by {movie['director'].title()}")

    return "\nEND of LIST"

#Operations 
operations = {
    "add" : add_movie,
    "list" : list_movies,
    "search" : search_movie
}

q = True
print("\nWelcome to the Film Flix Application! \nEnter an Operation \n")

while (q):

    #Obtain an INPUT OPERATION
    index = 0

    print("\nCHOOSE ONE OF THE OPERATIONS : ")
    for operation in operations:
        index = index + 1
        print(f"{index}. {operation}")

    operation_selected = input("Enter an Operation : ")

    #Perform Operation
    while True:
        if operation_selected in operations:
            print(operations[operation_selected]())
        else:
            print("Enter a Valid Operation!")
        
        break

    q = quit_function()