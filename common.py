#!/usr/bin/env python3

import random
import sys
import common

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']


def choices(e, n):
    """Renvoie une liste composée de n éléments tirés de e avec remise
    On pourrait utiliser random.choices, mais cette fonction n'est pas
    disponible dans les versions plus anciennes de Python
    """
    return [random.choice(e) for i in range(n)]



def evaluation (attempt,solution):
    """
    Fonction qui compare l'essai proposé par codebreaker à la solution
    de référence de codemaker.
    Les arguments sont donc l'essai de codebreaker et la solution de codemaker.
    Renvoie un couple de deux entiers: le nombre de bonnes couleurs bien placées
    et le nombre de bonnes couleurs mal placées.
    """
    #on commence par s'assurer que la combinaison proposée ait une longueur valide
    if len(attempt) != len(solution):
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")
    
    sol=[]
    #on transforme solution sous forme de liste afin de pouvoir modifier chaque caractère indépendamment 
    for j in range(len(solution)):
        sol.append(solution[j])
        
    #on initilise le nombre de plot bien placés à 0
    pbp=0
    #on initialise le nombre de plot bien et mal placés 0
    pbmp=0
    
    #on commence par chercher les plots bien placés en comparant le ième élément de solution avec le ième élément d'attempt
    for i in range(len(attempt)):
        if attempt[i]== sol[i]:
            pbp += 1 #si les deux sont les mêmes on implémente pbp
            
        #pour connaître les plots mal placés, on parcourt et compare tous les élément de solution pour chaque élément d'attempt
        for k in range(len(sol)):
            #si l'un des éléments d'attempt est le même que le ième élément de solution
            if attempt[i] == sol[k]: 
                #on remplace ce caractère par une chaîne vide car s'il est présent plusieurs fois dans attempt il faut le compter qu'une seule fois
                sol[k]='' 
                pbmp += 1 #puis on implémente pbmp
                break #on passe directement à la boucle suivante puisqu'on a trouvé une correspondance
    pmp=pbmp-pbp #enfin pour avoir uniquement les plots mal placés on soustrait le nombre de plots bien placés
    return (pbp,pmp)




def donner_possibles(attempt,evaluation):
    """
    Arguments: essai proposé par codebreaker puis l'evaluation
    renvoyée par codemaker pour cet essai.
    Renvoie l'ensemble des solutions encore possibles après la première évaluation.
    """
    import itertools
    #on créer combi_possible en variable globale afin de ne pas recommencer à zéro à chaque fois que codebreaker fait un essai
    global combi_possibles 
    
    #on rentre dans combi_possible toutes les combinaisons possibles de 4 couleurs parmis 8 avec l'ordre qui compte
    produit=itertools.product(COLORS,repeat=LENGTH)
    combi_possibles=set([chaine(q) for q in produit]) 

    return maj_possibles(combi_possibles,attempt,evaluation)




def chaine (q):
    """
    Cette fonction permet de prendre un tuple de 4 lettres pour le mettre sous
    la forme d'une seule chaîne de 4 caractères.
    L'argument est donc un quadruplet du type ('J','B','B','G') et renvoie
    une chaîne de caractère du type 'JBBG'.
    """
    combinaison='' #on initialise la variable dans laquelle on mettra notre chaîne de caractères 
    #pour chaque élément de l'argument
    for i in q: 
        combinaison+=i #on l'ajoute à la chaîne de caractère
    return combinaison
    




def maj_possibles(combi_possibles,attempt,evaluation):
    """
    Prend en arguments le set des combinaisons encore possibles, le dernier 
    essai effectué et l'évaluation associée.
    Renvoie une mise-à-jour des combinaisons encore possibles en prenant en compte
    le nouvel essai et son évaluation.
    """
    poss=combi_possibles.copy()
    #pour chaque élement de combi_possible
    for i in poss:
        #on regarde ce que renvoie l'évaluation du ième élément de combi_possible avec le dernier essai
        #si l'évaluation est différente de celle renvoyée par codemaker
        if common.evaluation(attempt,i)!=evaluation:
            #on supprime l'élément de combi_possible
            combi_possibles.remove(i)
    return combi_possibles
