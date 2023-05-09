def somme():
    s=1
    #pour i allant de 1 à 4096
    for i in range (1,4096):
        #on ajoute à s i fois la probabilité
        s+=(1/4096)*i
    return s

#on fait tourner le programme et on le rentre dans une variable
p=somme()
#on l'affiche
print(p)
