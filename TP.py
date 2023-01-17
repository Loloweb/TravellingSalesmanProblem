import random as rd
import numpy as np

def afficherMatrice(P):
    """
    fonction d'affichage d'une matrice numpy
    """
    for i in P:
        print(i)

def Carto(n):
    """
    fonction de génération d'une matrice aléatoire
    à diagonale vide des distances entre n villes
    """
    mat = np.zeros([n,n])   # on génère une matrice de zéros n*n
    for i in range(len(mat)):
        for j in range(i):
            if(i!=j):
                distance = rd.randrange(0,1000)
                mat[i,j] = distance     # la distance entre i et j est égale à celle entre j et i
                mat[j,i] = distance
    return mat

def Populat(n, m):
    """
    fonction prenant comme paramètres d'entrée le nombre n de villes et le
    nombre 2m de solutions (individus) que l'on souhaite générer et qui renvoie une matrice P
    de solutions aléatoires. Utilisée pour la population de départ
    """
    P = []
    villes = [i+1 for i in range(n)] # liste croissante des numéros de villes

    for i in range(m):
        solution = []
        solution.append(villes[0]) # on ajoute la ville numéro 1
        nb = rd.randint(1, n-1)

        for j in range(n-1):
            if villes[nb] not in solution :
                solution.append(villes[nb])
            else :
                while (villes[nb] in solution):
                    nb = rd.randint(1, n-1)
                solution.append(villes[nb])
        if solution in P:
            i -= 1
        P.append(solution)
    return P

def CalculAdapt(chemin):
    somme = 0
    for etape in range(len(chemin)-1):
        noeud1 = chemin[etape]
        noeud2 = chemin[etape+1]
        somme += distances[noeud1-1, noeud2-1]
    somme += distances[chemin[len(chemin)-1]-1, 0]
    return somme

def SelectElit(P):
    classement = {}
    for i in P:
        classement[CalculAdapt(i)] = i
    dictTrie = (sorted(classement.items())[0:int(len(classement)/2)])
    res =[]
    for value in dictTrie:
        res.append(value[1])
    return res

def SelectTourn(P):
    liste = P
    res = []
    for i in range(len(P)//2):
        elem1 = liste.pop(rd.randrange(0,len(liste)))
        elem2 = liste.pop(rd.randrange(0,len(liste)))
        if(CalculAdapt(elem1) < CalculAdapt(elem2)):
            res.append(elem1)
        else:
            res.append(elem2)
    return res

def Croisement(p1:list, p2:list, i:int, j:int):
    f1 = list()
    f1.append(p1[0])
    for i in p2[i:i+j]:
        f1.append(i)

    for j in p1[i+j+1:]:
        f1.append(j)

    return f1

def Croisement(p1:list, p2:list, i:int, j:int):
    fils1 = CroisementBis(p1,p2,i,j)
    fils2 = CroisementBis(p2,p1,i,j)
    return fils1, fils2

def CroisementBis(p1:list, p2:list, i:int, j:int):
    fils = list()
    fils.append(p1[0])
    i-= 1
    for k in p2[i:i+j] :
        fils.append(k)

    for j in p1[i+j:]:
        fils.append(j)

    tempin = list()
    tempout = list()
    for elem in range(fils) :
        if fils[elem] not in temp :
            tempin.append(fils[elem])
        else :
            tempout.append(fils[elem])

    if len(tempout):
        pass

    return fils

def Mutation(individu):
    i = random.randint(1, len(individu))
    j = random.randint(1, len(individu))
    individu[i], individu[j] = individu[j], individu[i]

    return individu

def Genetiq(n, m, t, c, iters):
    """
    fonction prend en entrée un entier n (nombre de villes), le nombre d'individus, 2m,
    dans la population initiale, le taux, t, de la population subissant une mutation à chaque itération,
    la méthode de sélection c choisie (élitiste ou par tournoi) et le nombre iters d'itérations.
    Cette fonction donne en sortie la solution retenue.
    """
    pass

distances = Carto(5)

if __name__ == '__main__':
    print(distances)
    solution = [[1,2,3,4,5],[1,5,3,2,4]]
    print(Populat(4,2))