from models.Movie import Movie
from models.Genre import Genre
from exceptions.InvalidTitleException import InvalidTitleException
from exceptions.InvalidAgeLimitException import InvalidAgeLimitException
from exceptions.InvalidGenreException import InvalidGenreException
from exceptions.InvalidYearException import InvalidYearExeption
import data
import csv

# Récupère le dernier id du fichier
def last_index():
    with open('data/movies.csv',encoding='utf-8') as csvfile:
        read = csv.reader(csvfile, delimiter=';')
        last_row = None
        for row in (read):
            last_row = row[0].split(',')[0]
            
    if last_row:
        return int(last_row) +1
            

# Ajoute un nouveau film au fichier movies.csv    
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
            id = last_index()
            my_movie = [id,titre,annee_production,genre,age_limite]
            with open("data/movies.csv", "a",newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(my_movie)
            print("Votre film à bien été enregistré !")
            return -1

# Supprimer un film
def delete_movie(value):
    # Lire toutes les lignes et les stocke dans une list, retire l'éléement qu'on souhaite supprimer
    with open("data/movies.csv", "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        lignes = [row for row in reader]
        lignes.pop(value)
    
    # Réécrire le fichier sans la ligne qu'on veut supprimer
    with open("data/movies.csv", "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(lignes)
    
    print("Suppression du film effectué")


# Modifier un film
def modify_movie(movie_number:int):
    delete_movie(movie_number) # On supprime le film qu'on souhaite modifier
    insert_movie() # On l'ajoute à la fin du fichier
    print("Modification du film effectué")

         
if __name__ == "__main__":

    while True:
        print("1. Ajouter un film")
        print("2. Modifier un film")
        print("3. Supprimer un film")
        print("5. Quitter")

        choice = input("Quelle opération voulez vous effectuer : ")
            
        match choice:
            case "1":
                insert_movie()
                print("\n")
            case "2":
                inputUser = int(input("Quel film souhaiter vous modifier ? : "))
                modify_movie(inputUser)
                print("\n")
            case "3":
                inputUser = input("Quel film souhaiter vous suipprimer ? : ")
                delete_movie(inputUser)
                print("\n")
            case "4":
                exit()
            case _:
                print("Erreur, commande incorrect")

