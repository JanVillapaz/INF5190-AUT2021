# Correction

### A1

- Le script qui télécharger les données est dans : `manage.py`
- la base de données db.db (situé dans le répértoire db) doit d'abord être créée

Consultez `README.md` pour creer la bd

### A2

Le Background Scheduler est exécuté dès que l'application est lancée

- Source : `app.py`

### A4

Veuillez naviguer vers la route `/api/installations?arrondissement=LaSalle` pour tester la fonctionnalité

- Source : `app.py`

### A5

La fonctionalité se trouve sur la route `/`. Dans la barre de recherche, entrez le nom d'un arrondissement et cliquez
sur le bouton `search`.

Cela ne fonctionnera pas avec la touche Entrée. La requête ajax est fait dans la fonction
`installation_query()` de `/static/js/script.js`.

- Source : `app.py`, `script.js`

### A6

La fonctionalité se trouve sur la route `/`. Sélectionnez un nom d'installation dans la liste déroulante pour tester la
fonctionnalité.

Le service REST associé est disponible à la route `/api/installations/nom?nom=Ovila-Légaré`.

La requête ajax est fait dans la fonction `installation_selection()` de `/static/js/script.js`.

- Source : `app.py`, `script.js`

### B1

Les notifications concernant les nouvelles installations sont envoyées par e-mail aux e-mails stockées
dans `emails.yaml`

Identifiant de connexion de l'expéditeur :

```
- E-mail : bj091047inf5190@gmail.com
- Password : JVillapaz123!
```

- Source : `manage.py`, `emails.py`

### B2

```
You currently have Essential access which includes access to Twitter API v2 endpoints only.
If you need access to this endpoint, you’ll need to apply for Elevated access via the Developer Portal.
```

- J'ai envoyé une demande d'accès élevé, mais il est maintenant en attente d'approbation.

### C1

Le service REST associé est disponible à la route `/api/installation/date/2021`.

- Source : `app.py`

### C2

Le service REST associé est disponible à la route `/api/installation/date/2021/XML`.

- Source : `app.py`

### C3

Le service REST associé est disponible à la route `/api/installation/date/2021/CSV`.

- Source : `app.py`

### F1

[HEROKU](https://jan-villapaz-projet-session.herokuapp.com)

## Fonctionnalités Réalisées

- [x] A1 - 15xp
- [x] A2 - 5xp
- [x] A4 - 10xp
- [x] A5 - 10xp
- [x] A6 - 10xp
- [x] B1 - 10xp
- [ ] B2
- [x] C1 - 10xp
- [x] C2 - 10xp
- [x] C3 - 5xp
- [ ] F1 - 20xp

#### XP totale acquise:

15 + 5 + 10 + 10 + 10 + 10 + 10 + 10 + 5 = 85xp


