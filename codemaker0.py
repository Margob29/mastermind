#!/usr/bin/env python3

import sys
import common


def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = ''.join(common.choices(common.COLORS, common.LENGTH))
    # Pour une version encore plus triviale, on pourrait aussi utiliser solution = ''.join([common.COLORS[0] for i in range(common.LENGTH)])


def evaluation_partielle(solution, attempt):
    """
    Cette fonction n'est pas correcte, elle n'implémente qu'une évaluation partielle
    """
    if len(solution) != len(attempt):
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")
    red = 0
    white = 0
    for i in range(len(solution)):
        if solution[i] == attempt[i]:
            red = red + 1
    return(red, white)


def codemaker(attempt):
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument)
    """
    global solution
    red, white = evaluation_partielle(solution, attempt)
    return(red, white)

