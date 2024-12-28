# Booktoscrap (Bêta)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
![Python version](https://img.shields.io/badge/Python-%5E3.12-blue.svg)
![BeautifulSoup4 4.12.3](https://img.shields.io/badge/BeautifulSoup4-%5E4.12.3-brightgreen)
![Requests ^2.32.3](https://img.shields.io/badge/Requests-%5E2.32.3-brightblue)

**Bookstoscrap** est un module Python conçu pour extraire (scraper) des données du site web [books.toscrape](https://books.toscrape.com/)

**Objectif du module :**
- Extraire certaines données,
- Transformer ces données,
- Charger ces données dans un dossier sous un format exploitable par l'utilisateur.

**Le résultat obtenu est sous la forme suivante :**

- **[Export]** - *Dossier regroupant toutes les extractions :*

    - **[Nom de la category]** - *Sous-dossiers au nom d'une catégorie :*

        - `Nom de la category.csv` - *Fichier recensant un livre par ligne contenant :*
            - **[title]** - *Titre du livre,*
            - **[product_page_url]** - *Lien URL de la page produit du livre,*
            - **[category]** - *Catégorie dans laquelle le livre est classé,*
            - **[review_rating]** - *Note sur 5,*
            - **[image_url]** - *Lien URL de l'image de couverture du livre,*
            - **[product_description]** - *Description du produit,*
            - **[universal_product_code (upc)]** - *Codification du produit,*
            - **[price_excluding_tax]** - *Prix hors taxes,*
            - **[price_including_tax]** - *Prix taxes comprises,*
            - **[number_available]** - *Quantité en stock.*

        - `Nom de la catégorie_upc_1aaa1111111111a.jpg` - Fichier image de la couverture d'un livre. 

**Le projet vise donc à faciliter et structurer l'analyse fastidieuse du site.**


## Prérequis à l'installation de Booktoscrap
- **Avoir l'outil [![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/) installé sur sa machine**, Poetry servira de gestionnaire de dépendances.
  - Comment **vérifier si Poetry est déja installé** sur ma machine ? 
  À l'aide d'un terminal en exécutant la commande `poetry --version`
  Si Poetry est déja installé, vous devriez voir un résultat du type `Poetry version 1.x.x`
  - Poetry n'est pas installé sur ma machine **comment l'installer ?**
  Toujours dans le terminal faire ce qui suit :
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
        
*Le mode d'installation peut différer selon la plateforme utilisée, si besoin consulter la page d'installation du site officiel de Poetry via : https://python-poetry.org/docs/#installing-with-the-official-installer*


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

**À ce stade l'installation du projet devrait être terminée.**


## Utilisation du module Booktoscrap
Pour lancer l'extraction des données, exécuter la commande suivante dans votre terminal. Le processus peut être long, le shell de votre terminal vous rendra la main une fois l'extraction entièrement terminée.
```bash
poetry run python -m booktoscrap
```
**Le shell vous rend la main une fois l'extraction entièrement terminée.**

Un répertoire nommé **Export** sera alors directement accessible à la racine du projet à l'aide de votre explorateur de fichier habituel.
```bash
├── booktoscrap
├── Export
├── poetry.lock
├── pyproject.toml
├── README.md
└── requirements.txt
```

**REMARQUE :** *Pour le déplacer ce fichier, il est préférable de le compresser préalablement, il pourrait être volumineux. Pensez à vérifier !*



