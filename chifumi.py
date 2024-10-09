import random
#fonction qui renvoi le choix de lordinateur
def choix_ordi():
    choix = random.choice(["p" , "f" , "c"])     
    return choix

#fonction qui renvoi le verdicte d'une partie
def verdict(joueur,ordinateur):
    if joueur == ordinateur:
        return 0 #egalite
    elif(joueur == "p" and ordinateur == "c" ) or \
        (joueur == "f" and ordinateur == "p" ) or \
        (joueur == "c" and ordinateur == "f" ):
        return 1 #l'ordinateur gagne
    elif joueur in ["p" , "f" , "c"]and ordinateur in ["p" , "f" , "c"]:
        return -1 #l'ordinateur gagne 
    else:
        return 2 #le joueur a entre "q"

#fonction qui simule une partie de pierre-feuille-siseaux
def partie():
    joueur = imput("Entrer votre choix(p pour pierre , f pour feuille , c pour ciseaux , q pour quitter):").lower()

    if joueur == "q":
        print("Vous avez quitter le jeux.")
        return 2 #quitter le jeux

    ordinateur = choix_ordi()
    print(f"Ordinateur a choisi : {ordinateur}")

    result = verdict(joueur , ordinateur)

    if result == 1:
        print("Vous avez gagné !")
    elif result == -1:
        print("L'ordinateur a gagné !")
    elif result == 0:
        print("Egalité.")
    else:
        print("Choix invalide.")
    
    return result

# Fonction qui gère le jeu complet et affiche les scores
def jeu_pfc():
    score_joueur = 0
    score_ordi = 0
    
    while True:
        resultat = partie()
        
        if resultat == 1:
            score_joueur += 1
        elif resultat == -1:
            score_ordi += 1
        elif resultat == 2:
            break
        
        print(f"Scores : Joueur {score_joueur}, Ordinateur {score_ordi}")

# Appel de la fonction principale pour lancer le jeu
jeu_pfc(1)

    
