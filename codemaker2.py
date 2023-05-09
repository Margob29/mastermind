import common


def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = ''.join(common.choices(common.COLORS, common.LENGTH))
    
    global combi_compatibles
    combi_compatibles=0

    global k
    k=0
    
    
def codemaker(attempt):
    """
    Fonction qui change la valeur de la solution mais en restant cohérent avec
    les évaluations déjà porposés.
    Elle prend en argument un essai et renvoie une evaluation en fonction de la nouvelle solution
    """
    global combi_compatibles
    global solution
    global k
    
    #si k=0, c'est que c'est notre première évaluation
    #dans ce cas pas la peine de changer la solution
    if k==0:
        red, white = common.evaluation(attempt, solution)
        combi_compatibles=common.donner_possibles(attempt,(red,white))
        k+=1 #on incrémente k pour savoir ensuite que ce n'est plus la première proposition
        return (red, white)
    
    #s'il ne reste qu'un seul élément dans combi_compatibles on a pas besoin de changer la solution
    elif len(combi_compatibles)==1:
        red,white=common.evaluation(attempt, solution)
        return red,white

    #si k=1 c'est que codebreaker a déjà créé combi_compatibles
    else:
        #on enlève l'essai de combi_compatibles pour que codebreaker ne gagne pas directement 
        combi_compatibles.remove(attempt)
        
        maxi=0
        
        #pour chaque élément du set
        for i in combi_compatibles:
            try_poss=combi_compatibles.copy()
            #on fait comme si on choisissait cet élément comme nouvelle solution et on met à jour try_poss
            try_poss=common.maj_possibles(try_poss,attempt,common.evaluation(attempt,i))
            #on compare ensuite la longeur de tout les try_poss et on ne conserve que la plus grande
            if len(try_poss)>maxi:
                maxi=len(try_poss)
                solution=i #notre nouvelle solution de vient celle qui a le plus grand set de combinaison encore possible avec son évaluation
       
        red, white = common.evaluation(attempt, solution) #on effectue la nouvelle évaluation
        combi_compatibles=common.maj_possibles(combi_compatibles,attempt,(red,white)) #on met à jour combi_compatibles
        return (red,white)