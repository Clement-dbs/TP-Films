import csv

# Récupère un film par son nom (il doit être correctement écrit)
def get_movie_by_name(movie_name:str):
    with open("write/data/movies.csv", "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if row[0].split(',')[1] == movie_name:
                return row
        return "aucun film n'a été trouvé"

# Récupère une list de films ne dépassant pas une limite d'ages
def get_movie_by_age_limit(age_limit:int):
    with open("write/data/movies.csv", "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        list_movies = []
        for row in reader:
            print(row[0].split(',')[4])
            if int(row[0].split(',')[4]) <= age_limit:
                list_movies.append(row)
        return list_movies

# Récupère une liste de films par genre
def get_movie_by_genre(genre:str):
    with open("write/data/movies.csv", "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        list_movies = []
        for row in reader:
            print(row[0].split(',')[3])
            if row[0].split(',')[3] == genre:
                list_movies.append(row)
        return list_movies
    
# Récupère une liste de films par annee
def get_movie_by_year(annee1:int, annee2:int):
    with open("write/data/movies.csv", "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        list_movies = []
        for row in reader:
            print(row[0].split(',')[2])
            if int(row[0].split(',')[2]) >= annee1 and int(row[0].split(',')[2]) <= annee2:
                list_movies.append(row)
        return list_movies
    



if __name__ == "__main__":
    print(get_movie_by_name("La La Land"))
    print(get_movie_by_age_limit(15))
    print(get_movie_by_genre("Action"))
    print(get_movie_by_year(1995,2010))