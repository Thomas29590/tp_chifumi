import random
#fonction qui renvoi le choix de lordinateur
def choix_ordi():
    choix = random.choice(["p" , "f" , "c"])     
    return choix

#fonction qui renvoi le verdicte d'une partie
def verdict(): 