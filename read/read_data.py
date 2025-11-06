import csv

# Récupère un film par son nom (il doit être correctement écrit)
def get_movie_by_name(movie_name:str):
    with open("write/data/movies.csv", "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if row[0].split(',')[1] == movie_name:
                return row
        return "aucun film n'a été trouvé"
