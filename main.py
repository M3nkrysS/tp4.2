"""
lucas beaudry tinkler
groupe: 401
création de personnages DnD
"""
from random import randint, choice
from dataclasses import dataclass


def de_six():
    atribut = []
    for i in range(4):
        roll = randint(1, 6)
        atribut.append(roll)
    atribut.sort()
    atribut.pop(0)
    resultat = sum(atribut)
    atribut.clear()
    return resultat


def noms():
    liste_nom = ["Bob", "Serge", "Marcus", "Jean-Yve", "Marie-Anne", "Sir Sacàmèche", "Adrienne"]
    nom = choice(liste_nom)
    return nom


def professions():
    liste_professions = ["barbare", "barde", "clerc", "druide", "ensorceleur", "guerrier", "magicien", "moine", "occultiste", "paladin", "rôdeur", "roublard"]
    profession = choice(liste_professions)
    return profession


@dataclass
class NPC:
    force: int = de_six()
    agilite: int = de_six()
    constitution: int = de_six()
    intelligence: int = de_six()
    sagesse: int = de_six()
    charisme: int = de_six()
    class_armur: int = randint(1, 12)
    nom: str = noms()
    race: str = "elf"
    espece: str = "elf noir"
    pv: int = randint(1, 20)
    proffession: str = professions()

    def afficher_caracteristiques(self):
        print(f"nom: {self.nom}\nrace: {self.race}\nespece: {self.espece}\nproffession: {self.proffession}\nclasse d'armur: {self.class_armur}")
        print(f"\npoints de vie: {self.pv}\nForce: {self.force}\nagilité: {self.agilite}\nconstitution: {self.constitution}\nintelligence: {self.intelligence}\nsagesse: {self.sagesse}\ncharisme: {self.charisme}")


class Kobold(NPC):
    def __init__(self):
        super().__init__()

    def attaquer(self):
        cible = NPC
        atteindre = randint(1, 20)
        de_huit = randint(1, 8)
        if atteindre == 1:
            print("\nvous avez roulez un 1.\nVouz écouez lamentablement")
        elif atteindre == 20:
            print(f"\nBravo!Vouz avez roulez un 20.\nVous faites {de_huit} points de dommage à l'ennemi")
            cible = self.pv - de_huit
        else:
            if atteindre >= NPC().class_armur:
                print("ca marche")


class Hero(NPC):
    def __init__(self):
        super().__init__(de_six(), de_six(), de_six(), de_six(), de_six(), de_six(), randint(1, 12), noms(), "elf", "elf noir", randint(1, 20), professions())


npc = NPC()
npc.afficher_caracteristiques()

k = Kobold()
k.attaquer()
