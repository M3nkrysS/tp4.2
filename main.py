"""
Lucas B.T.
Gr: 401
création de personnages D&D
"""
from random import randint
from dataclasses import dataclass


def roule_de(faces_de):
    de = randint(1, faces_de)
    return de


def roll_of_the_dices(nbr_de):
    resultat_de = []
    for i in range(nbr_de):
        de = roule_de(6)
        resultat_de.append(de)
    resultat_de.remove(min(resultat_de))
    valeur = sum(resultat_de)
    return valeur


@dataclass
class Atributs:
    force: int = roll_of_the_dices(4)
    agilite: int = roll_of_the_dices(4)
    constitution: int = roll_of_the_dices(4)
    intelligence: int = roll_of_the_dices(4)
    sagesse: int = roll_of_the_dices(4)
    charisme: int = roll_of_the_dices(4)


class NPC:
    def __init__(self):
        self.force: int = roll_of_the_dices(4)
        self.agilite: int = roll_of_the_dices(4)
        self.sagesse: int = roll_of_the_dices(4)
        self.charisme: int = roll_of_the_dices(4)
        self.intelligence: int = roll_of_the_dices(4)
        self.constitution: int = roll_of_the_dices(4)
        self.ac = randint(1, 12)
        self.nom = "oppenheimer"
        self.race = "arakocra"
        self.espece = "Rainbowplum"
        self.pv = randint(1, 20)
        self.proffession = "artificier"

    def afficher_characteristiques(self):
        print(f"Nom: {self.nom}\nRace: {self.race}\nEspèce: {self.espece}\nProffession: {self.proffession}\nPoints de vie: {self.pv}\nClasse d'armure: {self.ac}\nForce: ")
