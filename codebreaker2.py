import common

def init():
    """
    Initialisation de variables
    """
    global combi_possibles
    combi_possibles=0
    return


    
def codebreaker(evaluation_p):
    """
    Cette fonction renvoie une nouvelle proposition parmis celles encore possibles.
    Pour cela nous avons en argument l'évaluation du dernier essai.
    """
    global combi_possibles
    global attempt
    
    #s'il n'y a pas encore eu d'évaluation c'est qu'on a rien proposé
    if evaluation_p==None:
        #on prend donc une combinaison aléatoirement parmis les 4096 possibles
        attempt=''.join(common.choices(common.COLORS, common.LENGTH))
        return attempt
    
    #s'il existe une évaluation mais que combi_possible est vide c'est que c'est la première tentative
    elif evaluation_p!=None and combi_possibles==0:
        #on va donc choisir une combinaison parmis celles encore possible grâce à la fonction donner_possibles
        combi_possibles=common.donner_possibles(attempt,evaluation_p)
        attempt = ''.join(common.choices(list(combi_possibles),1))
        return attempt
    
    #s'il existe une évaluation et que combi_possible n'est pas vide c'est qu'on a déjà proposé plus de 2 essais
    else:
        #dans ce cas on utilise la focntion maj_possible pour choisir la nouvelle combinaison
        combi_possibles=common.maj_possibles(combi_possibles,attempt,evaluation_p)
        attempt= ''.join(common.choices(list(combi_possibles),1))
        return attempt