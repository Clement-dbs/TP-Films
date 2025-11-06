from models.Movie import Movie
from models.Genre import Genre
from exceptions.InvalidTitleException import InvalidTitleException
from exceptions.InvalidAgeLimitException import InvalidAgeLimitException
from exceptions.InvalidGenreException import InvalidGenreException
from exceptions.InvalidYearException import InvalidYearExeption
import data
import csv

# def last_index():
#     with open('write/data/movies.csv',encoding='utf-8') as f:
#         reader = csv.reader(f)
#         last_row = None
#         for row in reader:
#             last_row = row 
#             print(row)

#     if last_row:
#         return int(last_row[0])

def insert_movie():
    while True:
        try:
            titre = input("Entrez le titre du film : ")
            if(type(titre) != str):
                raise InvalidTitleException("Titre incorrecte")
            
            annee_production = input("Entrez l'année de production du film : ")
            if(annee_production.isalpha()):
                raise InvalidTitleException("L'année de production doit être des numéros")
            
            genre = input("Entrez le genre du film : ")

            # Exception genre à gerer
            # raise InvalidGenreException("Le genre entrée n'existe pas")
            
            age_limite = input("Entrez l'age limite du film : ")
            if(age_limite.isalpha()):
                raise InvalidTitleException("L'age rentré est invalide")
        except InvalidTitleException as e:
            print(e)
        except InvalidYearExeption as e:
            print(e)
        except InvalidGenreException as e:
            print(e)
        except InvalidAgeLimitException as e:
            print(e)

        else :
            movie = Movie(titre,annee_production,genre,age_limite)
            #id = Movie.nb_movie
            my_movie = [titre,annee_production,genre,age_limite]
            with open("write/data/movies.csv", "a", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                writer.writerow(my_movie)
            print("Votre film à bien été enregistré !")
            return -1
    
insert_movie()