import requests
from bs4 import BeautifulSoup

# URL du livre "Sorting the Beef from the Bull".
url = "http://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html"

# Envoyer une requête GET à la page
response = requests.get(url)

# Vérifier que la requête a réussi
if response.status_code == 200:
    print(f"The server answer with the status code {response.status_code}, well done!")
else:
    print(f"WARNING - You get a status code {response.status_code}, when you should get a 200 status code!")

# Créer un objet soup de la <class 'bs4.BeautifulSoup'> pour pouvoir parser un document html
soup = BeautifulSoup(response.text, 'html.parser')

# Cibler les élements maintenant que tout le document est disponible dans soup

# Récupérer les infos produit via le tag html avec des sélecteurs css <table class="table table-striped">
product_informations = soup.find('table', class_='table table-striped')

print(product_informations)
