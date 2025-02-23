
import random


class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage



class Viking(Soldier):

    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.name + " has received " +  str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"



class Saxon(Soldier):

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received " +  str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"



class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking_add):
        if isinstance(viking_add, Viking):
            self.vikingArmy.append(viking_add)


    def addSaxon(self, saxon_add):
        if isinstance(saxon_add, Saxon):
            self.saxonArmy.append(saxon_add)

    def vikingAttack(self):
        v = random.choice(self.vikingArmy)
        s = random.choice(self.saxonArmy)

        dam_sa = s.receiveDamage(v.attack())

        if s.health <= 0:
            self.saxonArmy.remove(s)

        return dam_sa

    def saxonAttack(self):
        u = random.choice(self.vikingArmy)
        i = random.choice(self.saxonArmy)

        dam_vi = u.receiveDamage(i.attack()) 

        if u.health <= 0 :
            self.vikingArmy.remove(u)

        return dam_vi

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."



