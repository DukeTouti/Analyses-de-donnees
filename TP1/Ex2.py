"""
 *	Exercice 2: Exploring the students' performance dataset

 *	Étudiants:
 *	    - HABBAZ Kamal <kamal.habbaz@uir.ac.ma>
 *	    - HATHOUTI Mohammed Taha <mohammed-taha.hathouti@uir.ac.ma>
 *	    - [Ajoutez d'autres membres si nécessaire]

 *	Groupes:
 *	    - Groupe TD: TDB
 *	    - Groupe TP: TPC

 *	Date: lundi 22 septembre 2025
"""


"Q1"
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("StudentsPerformance.csv")

"Q2"
print(df.head())

'''	
 *	Les cinq premières colonnes sont catégoriques (gender, race/ethnicity, parental level of education, lunch, test preparation course) et les
 *	trois colonnes suivantes sont numériques (math score, reading score, writing score)
'''

"Q3"
print(df.info())
print(df.describe())

'''
 *	- Non il ne manque aucune valeur, d'après df.info() les 1000 lignes sont remplies ;
 *	- La moyenne des notes en maths est de 66.08900 ;
 *	- La matière avec le plus grand ecart-type est l'expression ecrite avec un ecart-type de 15.195657 ;
 *	- 50% ne représente pas la moyenne mais la mediane, càd la note qui sépare la classe en deux, 50% des élèves ont obtenu en dessous de cette
 *	  valeur et les autres 50% ont obtenus au dessus de cette valeur ;	
	
 *				Tableau Explicatif des données donnez par la commande df.describe() (ChatGPT)	
	
 *	Ligne				Signification
	
 *	count	Nombre de valeurs non nulles dans la colonne (ici 1000 pour chaque score).
 *	mean	La moyenne de la colonne (somme des valeurs ÷ nombre de valeurs).
 *	std	L’écart type, qui mesure la dispersion des valeurs autour de la moyenne.
 *	min	La valeur minimale dans la colonne.
 *	25%	Le 1er quartile (Q1) → 25% des élèves ont un score ≤ cette valeur.
 *	50%	La médiane (Q2) → 50% des élèves ont un score ≤ cette valeur.
 *	75%	Le 3e quartile (Q3) → 75% des élèves ont un score ≤ cette valeur.
 *	max	La valeur maximale dans la colonne.
'''

"Q4"
print(df.sample(10))

"Visualisations"
								
"Q5"
plt.hist(df['math score'], bins=10, color='skyblue', edgecolor='black') 
# Je divise les notes en 10 intervalles qui seront représentés par la suite par 10 barres dans une couleur bleu-ciel avec une delimitation noir afin de différencier entre les barres

# Partie Titre
plt.title("Histogramme de distribution des notes de maths", fontsize=22) # Titre de l'histogramme avec une taille de 22 plus lisible que par défaut
plt.xlabel("Notes", fontsize=18) # Titre de l'axe des abscisses avec une taille de 18
plt.ylabel("Nombres d'élèves", fontsize=18) # Titre de l'axe des ordonnées avec une taille de 18

# Amélioration de l'affichage de l'histogramme
plt.xticks(np.arange(0, 101, 10)) # Afficher sur l'axe des abscisses toutes les dizaines en commençant à l'origine 0 et s'arrêtant à 100
plt.grid(True) # Afficher la grille pour une meilleur lecture

# Cohérence des axes, repositionner les axes pour coincider l'origine à (0,0)
ax = plt.gca() # Recuère l'axe actuel
ax.spines['left'].set_position('zero') # Permet d'aligner l'axe des ordonnées y au niveau de x=0
# pour aligner l'axe des abscisse il suffira de remplacer left par bottom qui fait référence enfait à la position de l'axe des ordonnées qui est à gauche et l'axe des abscisse qui est en bas

plt.show() # Affiche l'histogramme

"Q5"
sns.boxplot(x='gender', y='math score', data=df) # Diagramme en boîte à moustaches avec comme abscisse le genre et comme ordonnée les notes de maths

# Titres des axes et du Diagramme
plt.title("Diagramme de distribution des notes de maths par genre", fontsize=22)
plt.xlabel("Notes", fontsize=18)
plt.ylabel("Genre", fontsize=18)

# Affichage de la grille
plt.grid(True)
plt.yticks(np.arange(0, 101, 5)) # Fixer un intervalle petit pour une lecture plus précise

plt.show() # Affiche le diagramme

'''
 *	- Les principales informations qu'on peut extraire d'un diagramme en boîte à moustaches sont les mesures de tendances centrale et de
 *	  dispersion contenant la mediane (représentée par le trait noir à l'intérieur de la boite bleu), le premier et le troisième quartile, 
 *	  la note maximale et la note minimale (les extrémités des moustaches) et enfin les valeurs abérantes représentées par des points au-delà
 *	  des moustaches ;
 *	- Chez les étudiants de sexe féminin, il y a belle et bien des valeurs abérantes en dessous de la moustache ;
'''

"Q7"
plt.scatter(df['math score'], df['reading score']) # Nuage de points des notes de maths en abscisse et des notes de lecture en ordonée

# Titres des axes et du Diagramme
plt.title("Nuage de points des notes de maths et de lecture", fontsize=22)
plt.xlabel("Notes de maths", fontsize=18)
plt.ylabel("Notes de lectures", fontsize=18)

plt.grid(True)
plt.xticks(np.arange(0, 101, 5))
plt.yticks(np.arange(0, 101, 5))
ax = plt.gca()
ax.spines['left'].set_position('zero') 

plt.show()

'''
 *	- Il y a une association positive (positively associated) entre les notes de maths et les notes de lecture ;
'''

"Q8"
correlation_mx = df[['math score', 'reading score', 'writing score']].corr()
sns.heatmap(
	correlation_mx,
	annot=True, # Permet d'afficher les valeurs des corrélations sur les cases
	cmap='coolwarm', # Permet d'avoir une Heatmap plus facile à lire avec un dégradé du bleu au rouge
	annot_kws={"size": 18}, # Permet de controller la taille des valeurs des corrélations
)

plt.title("Matrice de corrélation des notes", fontsize=22)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.show()

'''
 *	- D'après cette Heatmap, les deux matières avec la relation la plus forte sont la lecture et l'expression écrite avec une corrélation de
 	  0.95 ;
'''









