import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
np.random.seed(35)

#Exercice 1 : Échantillonnage et Loi des Grands Nombres
def coin_flip_experiment(num_flips):
	probabilite = [0.5, 0.5]
	return np.random.choice(['Pile', 'Face'], size = num_flips, p = probabilite)

def plot_coin_flip_convergence(max_flips):
	# Simuler les lancers
	flips = coin_flip_experiment(max_flips)
    
	# Calculer la proportion cumulative de 'Face'
	cumulative_faces = np.cumsum(flips == 'Face')
	flip_numbers = np.arange(1, max_flips + 1)
	proportions = cumulative_faces / flip_numbers
   
	# Créer le graphique
	plt.figure(figsize=(10, 6))
	plt.plot(flip_numbers, proportions, label='Proportion de Face', linewidth=1)
	plt.axhline(y=0.5, color='r', linestyle='--', label='Probabilité théorique (0.5)')
   
	plt.xlabel('Nombre de lancers')
	plt.ylabel('Proportion de Face')
	plt.title('Convergence vers la Loi des Grands Nombres')
	plt.legend()
	plt.grid(True, alpha=0.3)
	plt.ylim([0.3, 0.7])  # Limiter l'axe y pour mieux visualiser
    
	plt.show()
    
	# Afficher la proportion finale
	print(f"Proportion finale de Face après {max_flips} lancers : {proportions[-1]:.4f}")

plot_coin_flip_convergence(10000)

# RÉPONSES AUX QUESTIONS - EXERCICE 1 :
# Question 1 : Comment la proportion de faces change-t-elle lorsque le nombre de lancers augmente ?
#	Réponse : La proportion de faces fluctue beaucoup au début (avec peu de lancers), puis se stabilise
#	progressivement autour de 0.5 à mesure que le nombre de lancers augmente. Les variations deviennent
#	de plus en plus petites.
#
# Question 2 : Qu'est-ce que cela démontre à propos de la Loi des Grands Nombres ?
#	Réponse : Cela démontre que lorsque le nombre d'expériences indépendantes augmente.
#	Plus on lance la pièce, plus on se rapproche de la probabilité théorique de 0.5.
#
# Question 3 : Essayez d'exécuter la simulation plusieurs fois. Obtenez-vous exactement le même résultat ?
#	Réponse : Oui, on obtient le même résultat car nous avons défini np.random.seed(35) au début.
#	Cette graine rend les résultats aléatoires reproductibles. Si on enlève cette ligne ou change
#	la valeur de la graine, les résultats varieront légèrement à chaque exécution, mais convergeront
#	toujours vers 0.5.

#Exercice 2 : Distributions de Probabilité Discrètes
def plot_binomial_distribution(n, p):
	k = np.arange(0, n+1)
	plt.figure(figsize=(10, 6))
	plt.stem(k, stats.binom.pmf(k, n, p), basefmt = ' ')
	plt.xlabel('Nombre de succès')
	plt.ylabel('Probabilité')
	plt.title(f'Distribution Binomiale (n={n}, p={p})')
	plt.grid(True, alpha=0.3)
	plt.show()

plot_binomial_distribution(20, 0.5)

# RÉPONSES AUX QUESTIONS - EXERCICE 2 :
# Question 1 : Que représente cette distribution en termes de scénario du monde réel ?
#	Réponse : Cette distribution (n=20, p=0.5) représente le nombre de succès dans 20 essais indépendants,
#	chacun ayant 50% de chance de succès. Par exemple : lancer une pièce 20 fois et compter le nombre
#	de faces, ou répondre à 20 questions vrai/faux au hasard, ou le nombre de clients sur 20 qui
#	achètent un produit quand le taux de conversion est de 50%.
#
# Question 2 : Comment la forme change si on augmente n à 50 ? Et si on change p à 0.7 ?
#	Réponse :
#		- Si n=50 : La distribution devient plus étalée (plus de valeurs possibles de 0 à 50)
#	et plus "lisse", se rapprochant d'une courbe en cloche (normale). Le pic reste autour de 25.
#		- Si p=0.7 : La distribution devient asymétrique, décalée vers la droite. Le pic se déplace
#	vers 14 (70% de 20), car il y a plus de chance d'avoir plus de succès.
#
# Question 3 : Une situation où cette distribution est utile ?
#	Réponse : si un médicament a 80% d'efficacité, combien de patients sur 50 répondront au traitement ?

#Exercice 3 : Espérance et Variance
def card_game_simulation(num_games):
	gains = [1, 5, 10, 0]
	
	prob_coeur = 12/52      # 12 cœurs sans l'as
	prob_as = 4/52          # 4 as
	prob_roi_pique = 1/52   # 1 roi de pique
	prob_autre = 35/52      # 35 autres cartes
    
	probabilites = [prob_coeur, prob_as, prob_roi_pique, prob_autre]
	resultats = np.random.choice(gains, size=num_games, p=probabilites)
    
	return resultats

def analyze_card_game(num_games):
	"""
	Analyse le jeu de cartes :
	- Exécute la simulation
	- Calcule et affiche la moyenne, variance et écart-type
	- Trace un histogramme des gains
	"""
	# a. Exécuter la simulation
	winnings = card_game_simulation(num_games)
	
	# b. Calculer et afficher les statistiques
	moyenne = np.mean(winnings)
	variance = np.var(winnings)
	ecart_type = np.std(winnings)
	
	print("=" * 50)
	print(f"Analyse de {num_games} parties du jeu de cartes")
	print("=" * 50)
	print(f"Moyenne des gains : ${moyenne:.4f}")
	print(f"Variance : {variance:.4f}")
	print(f"Écart-type : ${ecart_type:.4f}")
	print("=" * 50)
	
	# Calculer l'espérance théorique
	esperance_theorique = (1 * 12/52) + (5 * 4/52) + (10 * 1/52) + (0 * 35/52)
	print(f"Espérance théorique : ${esperance_theorique:.4f}")
	print("=" * 50)
	
	# c. Tracer un histogramme des gains
	plt.figure(figsize=(10, 6))
	plt.hist(winnings, bins=[0, 1, 5, 10, 11], edgecolor='black', alpha=0.7)
	plt.xlabel('Gains ($)')
	plt.ylabel('Fréquence')
	plt.title(f'Distribution des gains sur {num_games} parties')
	plt.xticks([0, 1, 5, 10])
	plt.grid(True, alpha=0.3, axis='y')
	
	# Ajouter une ligne verticale pour la moyenne
	plt.axvline(moyenne, color='r', linestyle='--', linewidth=2, 
				label=f'Moyenne: ${moyenne:.2f}')
	plt.legend()
	
	plt.show()
	
	return winnings

resultats = analyze_card_game(10000)

# RÉPONSES AUX QUESTIONS - EXERCICE 3 :
# Question 1 : Quelle est l'espérance de gain en jouant à ce jeu une fois ? Est-ce un jeu équitable ?
#	Réponse : L'espérance théorique est de $0.8077 (environ $0.81). Ce n'est PAS un jeu équitable
#	car l'espérance est positive. Un jeu équitable aurait une espérance de $0. Ici, en moyenne,
#	le joueur gagne environ 81 cents par partie, donc c'est avantageux pour le joueur.
#	Calcul : E(X) = 1*(12/52) + 5*(4/52) + 10*(1/52) + 0*(35/52) = 0.8077
#
# Question 2 : Comment l'écart-type est-il lié à la dispersion des résultats dans l'histogramme ?
#	Réponse : L'écart-type mesure la variabilité des gains autour de la moyenne. Un écart-type plus
#	élevé indique que les résultats sont plus dispersés/étalés dans l'histogramme. Ici, l'écart-type
#	est d'environ $2.17, ce qui montre qu'il y a une grande variabilité : on peut gagner $0, $1, $5
#	ou $10. Plus l'écart-type est grand, plus les barres de l'histogramme sont éloignées de la moyenne.
#
# Question 3 : Si vous jouiez 100 fois, vous attendriez-vous à toujours gagner le montant moyen ?
#	Réponse : NON, on ne gagnerait pas toujours exactement le montant moyen ($81 sur 100 parties).
#	À cause de la variabilité aléatoire, certaines séries de 100 parties donneront plus de $81,
#	d'autres moins. Mais en moyenne sur BEAUCOUP de séries de 100 parties, on se rapprocherait
#	de $81. La Loi des Grands Nombres garantit qu'avec suffisamment de parties,
#	la moyenne empirique convergera vers l'espérance théorique.

#Exercice 4 : Distributions de Probabilité Continues

def plot_normal_distribution(mean, std_dev):
	x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
	y = stats.norm.pdf(x, mean, std_dev)
    
	plt.figure()
	plt.plot(x, y, label=f'Normal(μ={mean}, σ={std_dev})')
	plt.xlabel('x')
	plt.ylabel('Density')
	plt.title('Normal Distribution')
	plt.legend()
	plt.grid(True)
	plt.show()

plot_normal_distribution(170, 10)


def plot_normal_distribution_shaded(mean, std_dev):
	x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
	y = stats.norm.pdf(x, mean, std_dev)
    
	plt.figure()
	plt.plot(x, y, label=f'Normal(moyenne={mean}, sigma={std_dev})')
    
	x_fill = x[(x >= mean - std_dev) & (x <= mean + std_dev)]
	y_fill = stats.norm.pdf(x_fill, mean, std_dev)
	plt.fill_between(x_fill, y_fill, alpha=0.3, label='1sigma')
    
	plt.xlabel('x')
	plt.ylabel('Densité')
	plt.title('Distribution normale')
	plt.legend()
	plt.grid(True)
	plt.show()

plot_normal_distribution_shaded(170, 10)

# RÉPONSES AUX QUESTIONS - EXERCICE 4 :
# Question 1 : Que pourrait représenter cette distribution dans un contexte du monde réel ?
#	Réponse : Une distribution normale avec moyenne=170 et écart-type=10 pourrait représenter
#	la taille (en cm) d'une population adulte...
#
# Question 2 : Approximativement quel pourcentage des données se situe dans un écart-type de la moyenne ?
#	Réponse : Environ 68% des données se situent dans un écart-type de la moyenne (règle empirique).
#	Dans notre cas : entre 160 et 180 cm, on trouve environ 68% de la population.
#
# Question 3 : Comment la forme changerait-elle si on diminuait l'écart-type à 5 ?
#	Réponse : La distribution deviendrait plus étroite et plus haute.
#	La courbe serait plus concentrée autour de la moyenne (170), avec moins de dispersion.
#	Les valeurs seraient plus regroupées.



