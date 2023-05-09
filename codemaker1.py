import common


def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = ''.join(common.choices(common.COLORS, common.LENGTH))
    
    
    
def codemaker(attempt):
    """
    Cette fonction utilise la fonction commune 'evaluation' afin de comparer
    l'essai de codebreaker avec la combinaison de référence.
    L'argument est donc l'essai.
    """
    global solution
    
    #on associe red aux plots bien placés et white aux plots mal placés que nous renvoie la fonction évaluation
    red, white = common.evaluation(attempt, solution) 
    
    return (red,white)