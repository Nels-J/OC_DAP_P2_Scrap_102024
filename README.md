# Booktoscrap
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
![Python version](https://img.shields.io/badge/Python-%5E3.12-blue.svg)
![BeautifulSoup4 4.12.3](https://img.shields.io/badge/BeautifulSoup4-%5E4.12.3-brightgreen)
![Requests ^2.32.3](https://img.shields.io/badge/Requests-%5E2.32.3-brightblue)

Bookstoscrap est un module Python conçu pour extraire (scraper) des données du site web https://books.toscrape.com/

**Objectif de ce module :**
- Absorber le contenu des pages du site,
- Extraire certaines données,
- Restituer à l'utilisateur sous un format exploitable.

**Le résultat obtenu est sous la forme suivante :**

- **[Export]** - *Dossier regroupant toutes les extractions :*

    - **[Nom de la category]** - *Sous-dossiers au nom d'une catégorie :*

        - `Nom de la category.csv` - *Fichier recensant un livre par ligne avec :*
            - **[title]** - *Titre du livre,*
            - **[product_page_url]** - *Lien URL de la page produit du livre,*
            - **[category]** - *Catégorie dans laquelle le livre est classé,*
            - **[review_rating]** - *Version de l'édition,*
            - **[image_url]** - *Lien URL de l'image de couverture du livre,*
            - **[product_description]** - *Description du produit,*
            - **[universal_product_code (upc)]** - *Codification du produit,*
            - **[price_excluding_tax]** - *Prix hors taxes,*
            - **[price_including_tax]** - *Prix taxes comprises,*
            - **[number_available]** - *Quantité en stock.*

        - `Nom de la catégorie_upc_1aaa1111111111a.jpg` - Fichier image de la couverture d'un livre. 

Le projet vise donc à faciliter et structurer l'analyse fastidieuse d'un site concurrent.


## Prérequis à l'installation de Booktoscrap
- **Avoir l'outil [![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/) installé sur sa machine**, Poetry servira de gestionnaire de dépendances.
  - Comment **vérifier si Poetry est déja installé** sur ma machine ?
    - A l'aide d'un terminal en exécutant la commande `poetry --version`
    - Si Poetry est déja installé, vous devriez voir un résultat du type `Poetry version 1.x.x`
      - Poetry n'est pas installé sur ma machine **comment l'installer ?**
        - Toujours dans le terminal faire ce qui suit :
          ```bash
          curl -sSL https://install.python-poetry.org | python3 -
          
          # Le mode d'installation peut différer selon la plateforme utilisé.
          # Si besoin consulter la page d'installation du site Poetry via :
          # https://python-poetry.org/docs/#installing-with-the-official-installer
          ```


## Installation
- **Vérifiez-les prérequis avant de passer à la suite.**

- **Cloner le projet :**
  - Le repo github est accessible ici : https://github.com/Nels-J/OC_DAP_P2_Scrap_102024
      ```bash
    # Pour cloner directement en SSH
      git clone git@github.com:Nels-J/OC_DAP_P2_Scrap_102024.git
      ```
  
- **Configurer son environnement virtuel :**
Un environnement virtuel créé dans le répertoire du projet est conseillé.
Pour configurer Poetry dans ce sens, exécuter la commande :
     ```bash
     poetry config virtualenvs.in-project true
     ```
- Installer les dépendances du projet à l'aide de la commande Poetry :

    ```bash
    poetry install
    ```
### À ce stade l'installation du projet devrait être terminé.

**À ce stade l'installation du projet devrait être terminée.**


## Lancer le module Booktoscrap
Pour lancer l'extraction des données exécuter la commande suivant dans votre terminal.


## Lancer le module Booktoscrap
Pour mettre en route,
```bash
poetry run python -m booktoscrap
```

