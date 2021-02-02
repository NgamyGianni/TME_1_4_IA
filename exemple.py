def lectureFichier(s): # Definition d'une fonction, avec un parametre (s). Ne pas oublier les ":"
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    monFichier.close() #Fermeture du fichier
    contenu[0]=contenu[0].split()     # ligne.split() renvoie une liste de toutes les chaines contenues dans la chaine ligne (separateur=espace)
    contenu[1]=contenu[1].split()
    return contenu
    # Commandes utiles:
    # n=int(s) transforme la chaine s en entier.
    # s=str(n) l'inverse
    # Quelques methodes sur les listes:
    # l.append(t) ajoute t a la fin de la liste l
    # l.index(t) renvoie la position de t dans l (s'assurer que t est dans l)
    # for s in l: s vaut successivement chacun des elements de l (pas les indices, les elements)


def createFichierLP(nomFichier,nombreVariables):
    monFichier=open(nomFichier,"w") #Ouverture en ecriture. Le fichier est ecrase s'il existe, cree s'il n'existe pas
    monFichier.write("Maximize\n")
    for i in range(0,nombreVariables): #Boucle i variant de 0 a NombreVariables-1
        monFichier.write("x"+str(i)+" ") #write pour ecrire. Indentation
        if (i<nombreVariables-1): # Syntaxe d'un test. 'and' et 'or' dans les expressions logique
            monFichier.write("+ ")
        else:
            monFichier.write("\n")
    monFichier.write("st\n") # Fin de l'indentation -> fin de la boucle
    monFichier.write("Binary\n")
    for i in range(0,nombreVariables):
        monFichier.write("x"+str(i)+" ")
    monFichier.write("\n")
    monFichier.write("end")
    monFichier.close()

def LLPrefEtu(nomFichier):
    LL = []
    f = open(nomFichier, "r")
    for line in f.readlines():
        LL.append(line.split()[2:])
    f.close()
    return LL[1:]

def LLPrefSpe(nomFichier):
    LL = []
    f = open(nomFichier, "r")
    for line in f.readlines():
        LL.append(line.split()[2:])
    f.close()
    return LL[2:]

def LI(nomFichier):
    L = []
    f = open(nomFichier, "r")
    for line in f.readlines():
        L.append(line.split()[0])
    f.close()
    return L[1:]

def LH(nomFichier):
    L = []
    f = open(nomFichier, "r")
    for line in f.readlines():
        L.append(line.split()[0])
    f.close()
    return L[2:]

def Lcapacity(nomFichier):
    L = []
    f = open(nomFichier, "r")
    t = f.readlines()
    f.close()
    return t[1].split()[1:]

def CEtudiant(fichierEtu, fichierSpe):
    Li = LI(fichierEtu)
    Lh = LH(fichierSpe)
    Lci = LLPrefEtu(fichierEtu)
    Lch = LLPrefSpe(fichierSpe)
    Lcap = Lcapacity(fichierSpe)
    libres = {e for e in Li}
    occup = [[] for i in range(len(Lh))]
    
    while len(libres) != 0:
        for e1 in Li:
            if e1 in libres:
                ie1 = int(e1)
                for e2 in Lci[ie1]:
                    ie2 = int(e2)
                    if occup[ie2] < Lcap[ie2]:
                        occup[ie2].append(e1)
                        libres.remove(e1)
                        break
                    else:
                        if Lch[e2].index(occup[ie2][len(occup[ie2])-1]) > Lch[ie2].index(e1):
                            tmp = occup[ie2].pop(len(occup[ie2])-1)
                            occup[ie2].append(e1)
                            libres.remove(e1)
                            libres.add(tmp)

    return occup


#def Q4(affect, matriceE, matriceS):
    """res = []

    for L in affect:
        for e in L:
            for cours in """

print(CEtudiant("PrefEtu.txt", "PrefSpe.txt"))

