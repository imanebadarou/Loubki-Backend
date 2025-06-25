# Loubki - API REST

Ce projet est une API REST pour le jeu **Loubki**, un jeu interactif de narration d'histoires.  
L'API est conçue avec **Flask** et **Flask-RESTX**, et utilise une base de données **SQLite**.

### Prérequis

Le projet utilise [Pipenv](https://pipenv.pypa.io/en/latest/) pour la gestion des dépendances.

- Python 3.12+
- Pipenv

### Installation

```bash
# Cloner le dépôt
git clone <url-du-repo>
cd Loubki-Backend

# Installer les dépendances
pipenv install
```

## Exécution

```bash
# Activer l'environnement virtuel
pipenv shell

# Lancer le serveur Flask
flask run

# Lancer le serveur Flask en mode développement
flask run --debug
```

## Documentation de l'API

Une documentation complète de l'API est disponible via Swagger à l'adresse `/` une fois le serveur lancé.