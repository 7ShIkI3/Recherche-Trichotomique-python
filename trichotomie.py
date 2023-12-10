def trichotomie(liste, valeur):
    valeurMoyenne1 = len(liste) // 2
    valeurMoyenne2 = valeurMoyenne1 // 4
    valeurMoyenne3 = valeurMoyenne1 + valeurMoyenne2
    
    if valeur == liste[valeurMoyenne1] or valeur == liste[valeurMoyenne2] or valeur == liste[valeurMoyenne3]:
        if valeur == liste[valeurMoyenne1]:
            return valeurMoyenne1, liste[valeurMoyenne1]
        elif valeur == liste[valeurMoyenne2]:
            return valeurMoyenne2, liste[valeurMoyenne2]
        elif valeur == liste[valeurMoyenne3]:
            return valeurMoyenne3, liste[valeurMoyenne3]
    elif valeur > liste[valeurMoyenne3]:
        index, value = trichotomie(liste[valeurMoyenne3:], valeur)
        return valeurMoyenne3 + index, value
    elif valeur > liste[valeurMoyenne1] and valeur < liste[valeurMoyenne3]:
        index, value = trichotomie(liste[valeurMoyenne1:valeurMoyenne3], valeur)
        return valeurMoyenne1 + index, value
    elif valeur > liste[valeurMoyenne2] and valeur < liste[valeurMoyenne1]:
        index, value = trichotomie(liste[valeurMoyenne2:valeurMoyenne1], valeur)
        return valeurMoyenne2 + index, value
    elif valeur < liste[valeurMoyenne2]:
        index, value = trichotomie(liste[:valeurMoyenne2], valeur)
        return index, value

nombre = [0,1,2,3,4,5,6,7,8,9,12,15,26,35,48,52,69,75,81,93,100]
resultat = trichotomie(nombre, 15)
#resultat est un tuple qui contient (index, liste[index]). 
index, value = resultat

if value in nombre:
    print(f"l'index est {index} et la valeur cherchée est {value}")
else:
    print(f"la valeur cherchée n'est pas dans la liste")

