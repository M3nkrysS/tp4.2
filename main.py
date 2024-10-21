"""
lucas beaudry tinkler
groupe: 401
création de personnages DnD
"""
from random import randint, choice


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

class NPC:
    def __init__(self, force, agilite, constitution, intelligence, sagesse, charisme, class_armur, nom, race, espece, pv, proffession):
        self.force = force
        self.agilite = agilite
        self.constitution = constitution
        self.intelligence = intelligence
        self.sagesse = sagesse
        self.charisme = charisme
        self.class_armur = class_armur
        self.nom = nom
        self.race = race
        self.espece = espece
        self.pv = pv
        self.proffession = proffession

    def afficher_caracteristiques(self):
        print(f"nom: {self.force}\nrace: {self.race}\nespece: {self.espece}\nproffession: {self.proffession}\nclasse d'armur: {self.class_armur}")
        print(f"\npoints de vie: {self.pv}\nForce: {self.force}\nagilité: {self.agilite}\nconstitution: {self.constitution}\nintelligence: {self.intelligence}\nsagesse: {self.sagesse}\ncharisme: {self.charisme}")


class Kobold(NPC):
    def __init__(self):
        super().__init__(de_six(), de_six(), de_six(), de_six(), de_six(), de_six(), randint(1, 12), noms(), "elf", "elf noir", randint(1, 20), professions())

    def attaquer(self):


    def subir_dommage(self):


class Hero(NPC):
    def __init__(self):
        super().__init__(de_six(), de_six(), de_six(), de_six(), de_six(), de_six(), randint(1, 12), noms(), "elf", "elf noir", randint(1, 20), professions())

    def attaquer(self):

    def subir_dommage(self):



npc = NPC(de_six(), de_six(), de_six(), de_six(), de_six(), de_six(), randint(1, 12), noms(), "elf", "elf noir", randint(1, 20), professions())
npc.afficher_caracteristiques()
