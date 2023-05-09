import common

def init():
    """
    Initialisation des variables
    """
    #création d'une liste où l'on va enregistrer les propositions que codebreaker fait
    global deja_prop
    deja_prop=[]
    return


    
def codebreaker(evaluation_p):
    """
    Cette fonction enregistre les porpositions déjà faites et vérifie
    que la nouvelle proposition ne soit pas dans cette liste.
    """
    #on créer une variable dans laquelle on met la proposition aléatoire
    nvlle_prop=''.join(common.choices(common.COLORS, common.LENGTH))
    
    #on vérifie que la nouvelle proposition ne soit pas identique à l'une des solutions déjà proposée 
    for k in range(len(deja_prop)):
        if deja_prop[k]==nvlle_prop:
            return codebreaker(evaluation_p) #si l'essai a déjà été proposé on recommence
        
    deja_prop.append(nvlle_prop) #s'il n'a pas encore été porposé on le rajoute dans la liste
    return nvlle_prop #et on renvoie ce nouvel essai
        
    
