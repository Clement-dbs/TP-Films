# TP Movie

## **1. Récupération du projet**

```bash
git clone https://github.com/Clement-dbs/TP-Films.git
```

## **2. Lancement du projet sous Docker**
1. Se positionner dans le dossier /read
2. Dans docker, excuter la commande suivante pour build l'image
**tp_movie_read**

```bash
    docker build -t tp_movie_read .
```
3. Se positionner dans le dossier /write puis excuter la commande pour build l'image **tp_movie_write**
   
```bash
    docker build -t tp_movie_read .
```
 
4. Pour executer l'une des 2 images :
   
   ```bash
       docker run -it --name movie_read tp_movie_read
   ```


## **3. Utilisation des applications**

Le projet **write** permet de :
* Ajouter un film
* Modifier un film
* Supprimer un film

  **Exemple :**

  ```bash
    # python read_data.py
    1. Récupère un film par son nom
    2. Récupère une liste de film par age limit
    3. Récupère une liste de film par genre
    4. Récupère une liste de film compris entre deux années
    5. Quitter
    Quelle opération voulez vous effectuer : 3
    Entrez un genre de film : Action
    ['3,The Dark Knight,2008,Action,12']
    ['6,Inception,2010,Action,12']
    ['7,The Matrix,1999,Action,16']
    ['17,Gladiator,2000,Action,12']
    ['19,The Avengers,2012,Action,12']
    ['22,Terminator 2: Judgment Day,1991,Action,12']
    ['27,Avatar,2009,Action,12']
    ['28,Raiders of the Lost Ark,1981,Action,12']
  ```
  
Le projet **read** permet de :
* Récupérer un film par son titre.
* Récupérer la liste des films ayant une limite d’âge inférieure ou égale à une valeur donnée.
* Récupérer la liste des films d’un certain genre.
* Récupérer la liste des films produits entre deux années données (année de début et année de fin).

  **Exemple :**

  ```bash
    # python manip-data.py
    1. Ajouter un film
    2. Modifier un film
    3. Supprimer un film
    5. Quitter
    Quelle opération voulez vous effectuer : 1
    Entrez le titre du film : Memento
    Entrez l'année de production du film : 1999
    Entrez le genre du film : Thriller
    Entrez l'age limite du film : 12
    Votre film à bien été enregistré !
  ```






```python

```
