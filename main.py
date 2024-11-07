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
        print(f"\npoints de vie: {self.pv}\nForce: {self.force}\nagilité: {self.agilite}\nconstitution: {self.constitution}\nintelligence: {self.intelligence}\nsagesse: {self.sagesse}\ncharisme: {self.charisme}\n")


class Kobold(NPC):
    def __init__(self):
        super().__init__()
        self.degat = randint(1, 6)

    def attaquer(self):
        atteindre = randint(1, 20)
        de_huit = randint(1, 8)
        if atteindre == 1:
            print("\nle kobold roule un 1.\nil échoue lamentablement")
        elif atteindre == 20:
            print(f"\nBravo!le kobold a roulé un 20.\nil fait {de_huit} points de dommage à l'ennemi")
            NPC().pv -= de_huit
        else:
            if atteindre >= NPC().class_armur:
                print(f"le kobold a atteint la cible.\nil fait {self.degat} point(s) de dégat")
                NPC().pv -= self.degat
            elif atteindre < NPC().class_armur:
                print("le kobold ne touche pas la cible")

        print(f"L'ennemi a {NPC().pv} pv")

    def subir_dommage(self):
        atteindre = randint(1, 20)
        if atteindre >= Kobold().class_armur:
            print(f"le kobold se fait toucher, il perd {self.degat} pv")
            Hero().pv -= self.degat
        elif atteindre < Kobold().class_armur:
            print("le kobold ne se fait pas touché")

        print(f"le kobold a {Kobold().pv} pv")


class Hero(NPC):
    def __init__(self):
        super().__init__()
        self.degat = randint(1, 6)

    def attaquer(self):
        atteindre = randint(1, 20)
        de_huit = randint(1, 8)
        if atteindre == 1:
            print("\nle hero a roulé un 1.\nil échoue lamentablement")
        elif atteindre == 20:
            print(f"\nBravo!le hero a roulé un 20.\nil fait {de_huit} points de dommage à l'ennemi")
            NPC().pv -= de_huit
        else:
            if atteindre >= NPC().class_armur:
                print(f"le hero a atteint la cible.\nil fait {self.degat} point(s) de dégat")
                NPC().pv -= self.degat
            elif atteindre < NPC().class_armur:
                print("le hero n'atteint pas la cible")

        print(f"L'ennemi a {NPC().pv} pv")

    def subir_dommage(self):
        atteindre = randint(1, 20)
        if atteindre >= Hero().class_armur:
            print(f"le hero se fait toucher, il perd {self.degat} pv")
            Hero().pv -= self.degat
        elif atteindre < Hero().class_armur:
            print("le hero ne se fait pas touché")

        print(f"le hero a {Hero().pv} pv")


npc = NPC()
npc.afficher_caracteristiques()

k = Kobold()
k.attaquer()
#k.subir_dommage()

#h = Hero()
#h.attaquer()
#h.subir_dommage()
