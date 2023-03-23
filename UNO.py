import random

types = ["nombres", "plus 2", "stop", "reverse", "plus 4", "autre couleur"]
couleurs = ["bleu", "rouge", "jaune", "vert"]
valeur = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class Carte:  # Définition de la classe
    def __init__(self, typeCarte, valeur,
                 couleur):  # constructeur (type, valeur, couleur)
        self.typeCarte = typeCarte
        self.valeur = valeur  # 1er attribut
        self.couleur = couleur
        return


class Tas:
    def __init__(self):  #à la création du tas,
        self.cartes = []

        for couleur in couleurs:  #pour chaque couleur
            self.cartes.append(Carte(types[0], 0, couleur))  #ajouter un 0
            for i in range(1, 10):  #pour chaque nombre de 1 à 9
                carte = Carte(types[0], i, couleur)  #on ajoute deux cartes
                self.cartes.append(carte)
                self.cartes.append(carte)

            for i in range(2):
                self.cartes.append(Carte(types[1], 0, couleur))
                self.cartes.append(Carte(types[2], 75, couleur))
                self.cartes.append(Carte(types[3], 0, couleur))
        for i in range(4):
            self.cartes.append(Carte(types[4], 45, "aucune"))
            self.cartes.append(Carte(types[5], 66, "aucune"))
        self.melanger()

    def melanger(self):
        random.shuffle(self.cartes)  #mélange toutes les cartes

    def piocher(self):
        return self.cartes.pop()

    def inserer(self, carte):
        self.cartes.insert(0, carte)


class Deck:  #classe deck capable de prendre des cartes, (poser, à venir)
    def __init__(self, taille):
        self.cartes = []
        self.prendre(taille)

    def prendre(self, nombre):
        print(len(tas.cartes))
        for i in range(nombre):
            self.cartes.append(tas.piocher())  #ajoute la carte qui est au dessus de la pioche

    def poser(self, nombre):
        global jeu
        print(len(decks.carte))
        carte = self.cartes.pop(nombre -1)
        jeu.append(carte)



def nombreJoueurs():  #donne le deck a chaque joueur
    print("Ce jeu est conçu pour 2 joueurs !")
    nbJoueurs = 2
    for i in range(nbJoueurs):  #pour chaque joueur
      decks.append(Deck(7))  #ajouter un nouveau deck de taille 7 au tableau de decks
      print("deck", i)
      for carte in decks[i].cartes:
        print("type:", carte.typeCarte, "/ valeur: ", carte.valeur, "/ couleur: ", carte.couleur)


def first():  #choisir la première carte et la changer si c'est un joker
    carte = tas.piocher()
    while carte.typeCarte in types[1:5]:
        tas.inserer(carte)  #si la carte piochée n'est pas un nombre, on la reinsère à la fin du tas
        carte = tas.piocher()
    print("type:", carte.typeCarte, "/ valeur: ", carte.valeur, "/ couleur: ", carte.couleur)
       #print la première carte du jeu (qui est toujours un nombre)
    return carte


joueur = 1


def plus4(carteJouée):  #fonction de la carte +4
    couleur = input("choisissez une couleur:")
    while not couleur in couleurs:
        couleur = input("cette couleur n'existe pas, veuillez recommencer")
        carteJouée.couleur = couleur  #les joueurs qui voudront jouer sur cette carte devront jouer la bonne couleur
    if joueur == 1:
      joueur == 2
      for i in range(4):
        decks.append(tas.piocher())  #piocher 4fois pour l'adversaire
    else:
        joueur == 1
        for i in range(4):
            decks.append(tas.piocher())    #piocher 4fois pour l'adversaire
            print(" Le joueur a pioché 4 cartes")
    print(carte)



def plus2(carteJouée):  #fonction de la carte +2
  global joueur
  joueur = 2
  for i in range(2):
    decks.append(tas.piocher())  #piocher 2fois pour l'adversaire


def autreCouleur(carteJouée):  #fonction de la carte autre couleur
  couleur = input("choisissez une couleur:")
  while not couleur in couleurs:
    couleur = input("cette couleur n'existe pas, veuillez recommencer")
    carteJouée.couleur = couleur  #les joueurs qui voudront jouer sur cette carte devront jouer la
                                      #bonne couleur

def reverse(carteJouée):          #fonction de la carte reverse
  global sens
  joueur = int("joueur")
  print("Le joueur ", joueur, " à mis une carte reverse, c'est donc encore à son tour !")
  sens = -1

def stop(carteJouée):        #fonction de la carte stop
  global sens
  joueur = int("joueur")
  print("Le joueur ", joueur + 1, " est stoppé, c'est encore au tour du joueur ", joueur)
  sens = -1

def nombre(carteJouée):
  if couleurs.carteJouée == couleurs.carte:
    return True
  elif valeur.carteJouée == valeur.carte:
    return True
  else:
      return False


tas = Tas()    #création du tas

decks = []

nombreJoueurs()    #affiche le nombre de joueur ainsi que leurs decks

print("------------------------------------------")

jeu = []


carte = first()  #affichage de la premiere carte

sens = 1
joueur = 1
#types = ["nombres", "plus 2", "stop", "reverse", "plus 4", "autre couleur"]
while len(decks) > 1:
    print("Tour du joueur", joueur)
    valeur = int(input("la valeur :"))
    couleur = input("La couleur: ")
    carteJouée = (valeur,couleur)

    if carteJouée.typeCarte == 0:
      if nombre() == True:
        decks.poser()

    if carteJouée.typeCarte == 4:                           #jouer un +4#si carte posée est +4
      decks.poser()
      plus4()                                               #faire fonction +4

    if  carteJouée.typeCarte == 1:                          #jouer un +2
      plus2()                                               #faire fonction +2

    if carteJouée.typeCarte == 5:          #jouer un change couleur  #si changer de couleur posé
      autreCouleur()                                        #faire choisir une autre couleur

    if carteJouée.typeCarte == 3:                    #si reverse posé inverser sens ou rejouer
      reverse()

    if carteJouée.typeCarte == 2:                                  #si stop posé
      stop()

    if carteJouée == "pioche":                              #piocher
      decks.poser()                                         #ajoute une carte au deck
