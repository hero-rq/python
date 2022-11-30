'''
class Wizard:
  def __init__(self, health, mana, armor):
    self.health = health
    self.mana = mana
    self.armor = armor
  def attack(self):
    print('파이어볼')

x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()
'''

class Dragon:
  def __init__(self, health, fire, attack):
    self.health = health
    self.fire = fire
    self.attack = attack
  def finale(self):
    print("All dead")

x = Dragon(health = 2100, fire = 2300, attack = 210)
print(x.health, x.fire, x.attack)
x.finale()
