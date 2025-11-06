
class Movie():

    def __init__(self, titre:str, anne_production:int,genre:str,age_limite:int):
        #id = Movie.nb_movie
        self.titre = titre
        self.annee_production = anne_production
        self.genre = genre
        self.age_limite = age_limite
            
    def __str__(self):
        print(f"==={self.titre}===\n")
        print(f"Année de production : {self.annee_production}")
        print(f"Genre : {self.genre}")
        print(f"Age limite : {self.age_limite}")

        