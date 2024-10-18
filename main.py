"""
lucas beaudry tinkler
groupe: 401
création de personnages DnD
"""
from random import randint

atribut = []


def de_six():
    for i in range(4):
        roll = randint(1, 6)
        atribut.append(roll)
    atribut.sort()
    atribut.pop(0)
    return atribut


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

npc = NPC(de_six(), de_six(), de_six(), de_six(), de_six(), de_six(), randint(1, 12), "serge", "", )