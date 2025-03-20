'''These classes are used to create a small RPG game with witches and warlocks that have one spell each.'''

'''This is the Super Class of Characters which is the parent class for Witches and Warlocks, and contains a method
named health_report which displays the given characters current health.'''
class Characters:
    def __init__(self, name, health):
        self.name= name
        self.health= health

    def health_report(self):
        print(self.name, "has health", self.health,".")


class Witches(Characters):
    def __init__(self, name, health):
        super().__init__(name,health)

    def cast_spell(self, target):
        self.target=target
        target.health -= 1
        print(self.name, 'cast Swoosh and dealt 1 damage to', target.name)

class Warlocks(Characters):
    def __init__(self, name, health):
        super().__init__(name,health)

    def cast_spell(self, target):
        self.target = target
        target.health -= 2
        print(self.name, 'cast Kaboom! It dealt 2 damage to', target.name)


Glenda= Witches("Glenda", 10)

Goliath= Warlocks("Goliath", 10)

Goliath_spell_count= 0
Glenda_spell_count= 0

print("Glenda's Spell List")
while Glenda_spell_count <= 2:
    Glenda.cast_spell(Glenda)
    Glenda.health_report()
    Glenda_spell_count +=1

print("                        ")

print("Goliath's Spell List")
while Goliath_spell_count <= 2:
    Goliath.cast_spell(Goliath)
    Goliath.health_report()
    Goliath_spell_count +=1





