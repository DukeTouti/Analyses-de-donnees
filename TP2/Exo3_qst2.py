"""
 *	Exercice 2: Exploring the students' performance dataset

 *	Étudiants:
 *	    - HABBAZ Kamal <kamal.habbaz@uir.ac.ma>
 *	    - HATHOUTI Mohammed Taha <mohammed-taha.hathouti@uir.ac.ma>
 *	    - KABORE Mohammed Sharif Jonathan <mohammad.kabore@uir.ac.ma>

 *	Groupes:
 *	    - Groupe TD: TDB
 *	    - Groupe TP: TPC

 *	Date: lundi 29 septembre 2025
"""


import matplotlib.pyplot as plt
import numpy as np


notes = [57, 66, 69, 71, 72, 73, 74, 77, 78, 78, 79, 79, 81, 91, 82, 83, 83, 88, 89, 94]

box = plt.boxplot(notes, patch_artist=True)

box['boxes'][0].set_facecolor('lightblue')
box['boxes'][0].set_edgecolor('black')

plt.title("Diagramme des notes", fontsize=22)
plt.ylabel('Notes', fontsize=18)


plt.yticks(np.arange(50, 100, 5))
plt.grid(True)
plt.show()
