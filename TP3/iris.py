"""
 *	Exercice 2: Exploring the students' performance dataset

 *	Étudiants:
 *	    - HABBAZ Kamal <kamal.habbaz@uir.ac.ma>
 *	    - HATHOUTI Mohammed Taha <mohammed-taha.hathouti@uir.ac.ma>

 *	Groupes:
 *	    - Groupe TD: TDB
 *	    - Groupe TP: TPC

 *	Date: lundi 06 ocotbre 2025
"""

"A-Q1"
from sklearn import *

"A-Q2"
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

"B-Q1"
iris = datasets.load_iris()

"B-Q2"
print("Les Clés du dictionnaire Iris :")
print(iris.keys()) # Affiche les clés (keys) du dictionnaire

"B-Q3"
print()
print(iris.data[:4]) # Affiche les 4 premières lignes [:4] de la matrice de données iris.data
print(iris.target) # Affiche la cible iris.target

"B-Q4"
print("\nLes noms des caractéristiques :")
print(iris.feature_names) # Affiche les noms des caractéristiques (feature_names)

print("\nLes noms des cibles :")
print(iris.target_names) # Affiche les noms des cibles (target_names)

"B-Q5"
species = iris.target_names[iris.target] #stocke le tableau contenant les noms (target_names) de chaque classe (target) dans la variable species 
print("\nLes noms de classes pour chaque point de donnée :")
print(species)

"B-Q6"
moyenne = iris.data.mean(0)
print("\nLa moyenne de chaque variable :")
print(moyenne)

ecart_type = iris.data.std(0)
print("\nL'ecart-type de chaque variable :")
print(ecart_type)

minimum = iris.data.min(0)
print("\nLe minimum de chaque variable :")
print(minimum)

maximum = iris.data.max(0)
print("\nLe maximum de chaque variable :")
print(maximum)

"B-Q7"
df = pd.DataFrame(data = iris.data, columns = iris.feature_names)

"B-Q8"
df.hist(bins=12, figsize=(10, 8), color='skyblue', edgecolor='black') # Histogramme, bins fixé à 12.
plt.suptitle('Histogrammes des caractéristiques du dataset Iris', y=1.02) # Titre de l'histogramme
plt.tight_layout() # Permet d'organiser la page du graphe pour faire en sorte que rien ne se chevauche
plt.show() # Affiche l'Histogramme

"B-Q9"
correlation_mx = df.corr() # Heatmap de corrélation entre les variables

# plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation_mx,
    annot=True,           # Affiche les valeurs sur les cases
    cmap='coolwarm',
    fmt='.2f',            # Float avec 2 chiffres après la virgule
    square=True,          # Cases carrées
    linewidths=0.5,       # Lignes entre les cases
)
plt.title("Heatmap de corrélation des caractéristiques Iris", fontsize=14)
plt.xticks(rotation=0)
plt.show()

"""
 * On remarque que 'sepal width' est le moins en concordences avec les autres variables on peut bien le retirer de la Heatmap ;
 * On voit qu'il y a une très très forte correlation entre la longueur et la largeure d'une pétale, on en deduit qu'elles sont probbalement
 * proportionnelles ;
"""

"B-Q10"
df['species'] = species # Rajoute la colonne 'species' au dataset
print(df.head()) # Affiche les 5 premières lignes du dataset

"Q11"
df['species'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Fréquence de chaque espèce dans le dataset Iris", fontsize=14)
plt.xlabel("Espèce", fontsize=12)
plt.ylabel("Fréquence", fontsize=12)
plt.xticks(rotation=0)    # Oriente les noms des especes (0 = horizontale, 90 = vertical, 45 = incliné vers la droite, 135 = incliné vers la gauche)
plt.show()

"""
 * D'après les résultats (50 individus par espèce), il s'agit d'un jeu de données équilibré, les classes ont chacune la même taille d'échatillon.
 * Cependant ce n'est peut être pas représentatif de la répartition réelle des espèces d'iris concernées, il se peut que certaines de ces espèces
 * soit plus rare et donc le dataset sera équilibré pour l'apprentissage si en on prand autant que pour les autre mais représentatif de la distri-
 * bution naturelle.
"""
"Q12"
sns.boxplot(x='species', y='petal length (cm)', data=df) # Diagramme en boîte à moustaches avec comme abscisse l'espece et comme ordonnée la longueur des pétales 'petal length (cm)' en centimetres

# Titres des axes et du Diagramme
plt.title("Diagramme de distribution de la longueur des pétales par espèce d'Iris", fontsize=22)
plt.xlabel("Espèce", fontsize=18)
plt.ylabel("Longueur d'un pétale (cm)", fontsize=18)

# Affichage de la grille
plt.grid(True)
plt.yticks(np.arange(0, 7.2, 0.1)) # Fixer un intervalle petit pour une lecture plus précise

plt.show() 










