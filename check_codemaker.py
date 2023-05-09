import common

def check_codemaker (log):
    """
    Fonction qui prend en entrée un fichier texte composé d'essais successifs 
    avec leur évaluation associée.
    Elle renvoie si codemaker a triché de façon visible ou non
    """

    with open(log,"r") as fichier:
        #on rentre chaque ligne du fichier texte dans une liste
        jeu=fichier.readlines()
        #on prend l'avant dernier élément, qui est le dernier essai et donc la solution
        solution=jeu[-2][0:4]
        
    for k in range(len(jeu)):
        #si k est pair on est sur une combinaison
        if k%2==0:
            #on enregistre cette combinaison comme essai
            attempt=jeu[k][0:4] 
            #et on fait l'évalaution avec la solution
            evaluation_r=common.evaluation(attempt,solution)
            
        #si k est impair on est sur une évaluation
        else:
            #on converti donc cette évaluation du fichier texte en format (red,white)
            red=int(jeu[k][0])
            white=int(jeu[k][2])
            evaluation_t=red,white
            #puis on compare cette évaluation avec celle calculée pour la solution et l'essai
            #si ce ne sont pas les mêmes on est sûr que codemaker a changé de solution pendant le jeu
            if evaluation_r!=evaluation_t:
                print("Codemaker a triché")
                break
    #si toutes les évaluations sont cohérentes on ne peut que affirmer que codemaker n'a pas triché de façon visible.
    print("Codemaker n'a pas triché de façon visible")