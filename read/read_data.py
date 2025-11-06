import csv

# Récupère un film par son nom (il doit être correctement écrit)
def get_movie_by_name(movie_name:str):
    with open("data/movies.csv", "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if row[0].split(',')[1] == movie_name:
                return row
        return "aucun film n'a été trouvé"

# Récupère une list de films ne dépassant pas une limite d'ages
def get_movie_by_age_limit(age_limit:int):
    with open("data/movies.csv", "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        list_movies = []
        for row in reader:
            if int(row[0].split(',')[4]) <= age_limit:
                list_movies.append(row)
        
        for movie in list_movies:
            print(movie)

        return list_movies

# Récupère une liste de films par genre
def get_movie_by_genre(genre:str):
    with open("data/movies.csv", "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        list_movies = []

        for row in reader:
            if row[0].split(',')[3] == genre:
                list_movies.append(row)

        for movie in list_movies:
            print(movie)

        return list_movies
# Récupère une liste de films par annee
def get_movie_by_year(annee1:int, annee2:int):
    with open("data/movies.csv", "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        list_movies = []
        for row in reader:
            if int(row[0].split(',')[2]) >= annee1 and int(row[0].split(',')[2]) <= annee2:
                list_movies.append(row)

        for movie in list_movies:
            print(movie)

        return list_movies
    

if __name__ == "__main__":

    while True:
        print("1. Récupère un film par son nom")
        print("2. Récupère une liste de film par age limit")
        print("3. Récupère une liste de film par genre")
        print("4. Récupère une liste de film compris entre deux années")
        print("5. Quitter")

        choice = input("Quelle opération voulez vous effectuer : ")
        
        match choice:
            case "1":
                inputUser = input("Entrez un nombre de film : ")
                print(get_movie_by_name(inputUser))
                print("\n")
            case "2":
                inputUser = int(input("Entrez une limite d'age : "))
                get_movie_by_age_limit(inputUser)
                print("\n")
            case "3":
                inputUser = input("Entrez un genre de film : ")
                get_movie_by_genre(inputUser)
                print("\n")
                
            case "4":
                input1 = int(input("Entrez une période entre 2 dates : "))
                input2 = int(input("Entrez une période entre 2 dates : "))
                get_movie_by_year(input1,input2)
                print("\n")
            case "5":
                exit()
            case _:
                print("Erreur, commande incorrect")
                    


    