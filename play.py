#!/usr/bin/env python3

import common

import codemaker0
import codemaker1
import codemaker2

import codebreaker0
import codebreaker1
import codebreaker2

def play(codemaker, codebreaker):
    """
    Fonction principale de ce programme :
    Fait jouer ensemble le codebreaker et le codemaker donnés en arguments
    """
    n_tries = 0
    codebreaker.init()
    codemaker.init()
    evaluation_p = None
    print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        attempt = codebreaker.codebreaker(evaluation_p)
        (red, white) = codemaker.codemaker(attempt)
        n_tries += 1
        print("Essai {} : {} ({},{})".format(n_tries, attempt, red, white))
        evaluation_p = (red, white)
        if red >= common.LENGTH:
            print("Bravo ! Trouvé {} en {} essais".format(attempt, n_tries))
            #break
            return n_tries
        

def play_human_against_codemaker(codemaker):
    """
    Fait jouer l'utilisateur humain (au clavier) dans le role du codebreaker
    contre un codemaker donné en argument
    """
    n_tries = 0
    codemaker.init()
    evaluation_p = None
    print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        attempt = input("Saisir combinaison: ")  # On lit une combinaison au clavier au lieu d'appeler le codebreaker (qui sera donc joué par un humain)
        if len(attempt) != 4:
            print("Combinaison invalide (pas la bonne taille)")
            continue
        (red, white) = codemaker.codemaker(attempt)
        n_tries += 1
        print("Essai {} : {} ({},{})".format(n_tries, attempt, red, white))
        evaluation_p = (red, white)
        if red >= common.LENGTH:
            print("Bravo ! Trouvé {} en {} essais".format(attempt, n_tries))
            break
        


def play_human_against_codebreaker(codebreaker):
    """
    Fait jouer l'utilisateur humain (au clavier) dans le role du codemaker
    contre un codebreaker donné en argument
    """
    n_tries = 0
    codebreaker.init()
    evaluation_p = None
    print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        attempt = codebreaker.codebreaker(evaluation_p)
        print('Combinaison proposée: {}'.format(attempt))
        red = int(input('Saisir nombre de plots rouges: '))
        white = int(input('Saisir nombre de plots blancs: '))
        n_tries += 1
        print("Essai {} : {} ({},{})".format(n_tries, attempt, red, white))
        evaluation_p = (red, white)
        if red >= common.LENGTH:
            print("Le codebreaker a trouvé {} en {} essais".format(attempt, n_tries))
            break


# Les lignes suivantes sont à modifier / supprimer selon ce qu'on veut faire, quelques exemples :

# Faire jouer ensemble codemaker0.py et codebreaker0.py pour 5 parties :

for i in range(5):
    play(codemaker1, codebreaker1)

#  Faire jouer un humain contre codemaker0.py :
import codemaker2
play_human_against_codemaker(codemaker2)


## Et plus tard, vous pourrez faire jouer vos nouvelles version du codebreaker et codemaker :
import codemaker1
play_human_against_codemaker(codemaker1)

#import codebreaker2
import codemaker2
play(codemaker2, codebreaker2)

# %% Pour la question 3, création d'une fonction et affichage de l'histogramme du nombre d'essais par partie
def plusieurs_play(codemaker,codebreaker,nbr):
    """
    Cette fonction sert à faire jouer codemaker contre codebreaker un nombre de fois donné.
    Elle enregistre ensuite le nombre d'essai réalisé pour chaque partie.
    Les arguments sont le codemaker puis le codebreaker que l'on veut faire jouer
    suivi du nombre de parties que l'on veut réaliser.
    """
    donnees=[]
    for i in range(nbr):
        #à chaque partie on ajoute le nombre d'essai dans donnees
        donnees.append(play(codemaker, codebreaker))
    return donnees

import matplotlib #pour tracer l'histogramme
import numpy
import statistics
#on créer une variable qui récupère les données après les 100 parties
resultat=plusieurs_play(codemaker1,codebreaker0,100)
# on affiche un graphique en barre qui met une barre de 1 à 100 (pour les 100 parties) et qui associe la valeur de résultat à chaque barre
matplotlib.pyplot.bar(numpy.arange(100),resultat)
#on nomme les x et les y 
matplotlib.pyplot.xlabel("Numéro de la partie")
matplotlib.pyplot.ylabel("Nombre d'essais")
# on affiche également la moyenne du nombre d'essais par partie
print("La moyenne est de: ",statistics.mean(resultat))

# %% Pour la question 4, création d'une fonction et affichage du gain en nombre d'essai entre codebreaker0 et codebreaker1
def plusieurs_play2(codemaker,codebreaker,nbr,esp):
    """
    Cette fonction sert à faire jouer codemaker contre codebreaker un nombre de fois donné.
    Elle enregistre ensuite le gain en nombre d'essai pour chaque partie.
    Les arguments sont le codemaker puis le codebreaker que l'on veut faire jouer
    suivi du nombre de parties que l'on veut réaliser ainsi que l'espérance à laquelle on veut le comparer.
    """
    donnees=[]
    for i in range(nbr):
        #pour avoir le gain on soustrait le nombre d'essais de codebreaker1 à l'espérance de codebreaker0
        donnees.append(esp-(play(codemaker, codebreaker)))
    return donnees

import matplotlib #pour tracer l'histogramme
import numpy
import statistics
resultat=plusieurs_play2(codemaker1,codebreaker1,100,4096)
matplotlib.pyplot.bar(numpy.arange(100),resultat)
matplotlib.pyplot.xlabel("Numéro de la partie")
matplotlib.pyplot.ylabel("Gain en nombre d'essais")
print("Gain moyen de: ",statistics.mean(resultat))
    

# %% Question 7 création d'une fonction et affichage du gain en nombre d'essai entre codebreaker1 et codebreaker2

import matplotlib #pour tracer l'histogramme
import numpy
import statistics
resultat=plusieurs_play2(codemaker1,codebreaker2,100,2048.5)
matplotlib.pyplot.bar(numpy.arange(100),resultat)
matplotlib.pyplot.xlabel("Numéro de la partie")
matplotlib.pyplot.ylabel("Gain en nombre d'essais")
print("Gain moyen: ",statistics.mean(resultat))
print("Nombre d'essais moyen avec codebreaker2: ", statistics.mean(plusieurs_play(codemaker1,codebreaker2,100)))

# %% Question 8

import matplotlib #pour tracer l'histogramme
import numpy
import statistics
resultat=plusieurs_play2(codemaker2,codebreaker2,100,5.57)
matplotlib.pyplot.bar(numpy.arange(100),resultat)
matplotlib.pyplot.xlabel("Numéro de la partie")
matplotlib.pyplot.ylabel("Gain en nombre d'essais")
print("Gain moyen avec codemaker2: ",statistics.mean(resultat))
print("Nombre d'essais moyen avec codebreaker2 et codemaker2: ",statistics.mean(plusieurs_play(codemaker2,codebreaker2,10)))

# %% Question 11

def play_log(codemaker, codebreaker, nom):
    """
    Fonction qui fait jouer le codemaker et le codebreaker donnés en argument.
    Pour chaque essai de codemaker elle écrit cet essai ainsi que l'évaluation
    associée dans un fichier texte dont le nom est donné en troisième argument.
    """
    n_tries = 0
    codebreaker.init()
    codemaker.init()
    evaluation_p = None
    #on créer une variable qui va contenir le nom du fichier avec l'argument de la fonction
    fichier=nom+'.txt' 
    #on créer le fichier text avec le nom voulu
    log=open(fichier,"x")
    
    while True:
        attempt = codebreaker.codebreaker(evaluation_p)
        (red,white) = codemaker.codemaker(attempt)
        n_tries += 1
        #on ouvre le fichier texte
        with open(fichier,"a") as log:
            #on ajoute l'essai
            log.write(attempt)
            #et on revient à la ligne
            log.write("\n")
        
        evaluation_p = (red,white)
        #on ouvre le fichier texte
        with open(fichier,"a") as log:
            #on ajoute le nombre de bonnes couleurs bien placées en format string
            log.write(str(red))
            #on met une virgule pour séparer les deux
            log.write(',')
            #on ajoute le nombre de bonnes couleurs mal placées en format string
            log.write(str(white))
            #on revient à la ligne
            log.write("\n")
            
        if red >= common.LENGTH:
            break