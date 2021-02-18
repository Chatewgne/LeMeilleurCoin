# LeMeilleurCoin

Démonstration technique Django : site de petites annonces.

(Réalisé avec Python 3.9.1, environnement local avec [Pyenv](https://realpython.com/intro-to-pyenv/))



## Le projet

Le projet est divisé en deux applications Django, une pour la gestion des utilisateurs ```accounts``` et une pour la gestion des annonces ```adverts```.

Les fonctionnalités incluses sont :
- Créer un compte utilisateur
- Se connecter
- Lister les annonces existantes
- Voir les détails d'une annonce (dont le numéro de téléphone de contact)
- Poster une annonce
- Se déconnecter

Seuls les utilisateurs connectés ont accès aux 4 dernières fonctionnalités, car LeMeilleurCoin se soucie de la confidentialité des données utilisateur en particulier les numéros de téléphones. 

Les annonces ont une relation one-to-many avec les utilisateurs (un utilisateur peut poster plusieurs annonces, qui doivent être supprimées quand l'utilisateur est supprimé).

Les utilisateurs possèdent un attribut ```phone_number```, obligatoire dans la création du compte, qui permet d'afficher cette information dans toutes les annonces qu'ils postent. Le numéro de téléphone doit être au format international (+33612345678).

Une annonce se compose d'un titre, d'une description, d'une photo et d'un prix. La photo n'est pas obligatoire.

En affichant le détail d'une annonce on obtient aussi le nom de l'utilisateur qui l'a postée, sa date de création, et le numéro de téléphone de l'auteur.




## Lancer l'application

Pour lancer le serveur de développement :

```
pip install -r requirements.txt
python manage.py runserver
```

(Pas besoin de gérer les migrations car j'ai poussé la base de données SQLite pré-remplie avec des annonces d'exemple. Bien sûr ça n'est pas une bonne pratique hors de ce contexte.)

Ensuite se rendre sur ```http://127.0.0.1:8000/accounts/login``` pour commencer la navigation. En premier lieu, se créer un compte (attention le numéro de téléphone doit être au format international (+33612345678)). Quand le compte sera créé vous serez redirigé vers la page de connexion, après laquelle vous accèderez aux annonces. 



## Lancer les tests unitaires

Les tests unitaires sont dans ```lemeilleurcoin/tests.py```.

```
python manage.py test
```
A titre indicatif, un test de couverture réalisé avec [coverage](https://coverage.readthedocs.io/en/coverage-5.4/) mais à prendre avec des pincettes.
![coveraqge](./coverage.png)



## Pistes d'améliorations

- Set up de production : docker-compose avec une "vraie" base de données (mongo, postgres...)
- Pouvoir supprimer ou metre à jour son annonce (demande de gérer les permissions, seul le créateur de l'annonce peut la modifier)
- Enlever le reste de mélange de français/anglais car je n'ai pas surchargé la totalité des labels
- Exhaustivité et qualité des tests toujours perfectibles
- Sécurité : les mots de passe/tokens passent en clair sur le réseau tant qu'on n'implémente pas HTTPS/SSL (pas simple avec le serveur de développement mais **obligatoire** en production)
- Sécurité : attention aux secrets dans les settings Django à ne pas pousser sur GitHub normalement (SECRET_KEY)
- Sécurité : pentest à faire au niveau des formulaires (inputs malveillants) 


[CSS par AndyBrewer](https://andybrewer.github.io/mvp/)