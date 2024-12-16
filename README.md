# Outil de scrapping.

L'objectif de cet outil est d'automatiser le scrapping du site https://books.toscrape.com/ à des fins d'études marketing pour l'entreprise.
Il facilite ainsi l'étude concurrentielle en agrégeant des données utiles depuis ce site.

## Préalable
- Avoir installé Poetry qui servira de gestionnaire de dépendances

## Installation
- Vérifiez-les prérequis avant de passer à la suite.

- Cloner le projet :
  - Le projet est accessible 
      ```bash
      git clone git@github.com:Nels-J/OC_DAP_P2_Scrap_102024.git
      ```
  
- Configurer son environnement virtuel :
Par défaut, Poetry crée un environnement virtuel pour chaque projet dans un cache. 
Il est préferable que l'environnement virtuel soit créé dans le même répertoire du projet,
pour cela, on exécute cette commande qui défini cette configuration :
     ```bash
     poetry config virtualenvs.in-project true
     ```
- Installer les dépendances avec le gestionnaire de dépendances Poetry :
    ```bash
    poetry install
    ```
### À ce stade l'installation du projet devrait être terminé.