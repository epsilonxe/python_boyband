from random import random

class Character():
	def __init__(self):
		self.health = 0
		self.attack = 0
		self.name = ''

	def showStat(self):
		print(f'[{self.name}] Health = {self.health}, Attack = {self.attack}')

	def isDead(self):
		if self.health <= 0:
			return True
		else:
			return False

	def doAttack(self, foe):
		x = random()
		y = type(self).__name__
		if x >= 0.2 and y == 'Human':
			cri_attack = 1.5 * self.attack
			foe.health = foe.health - cri_attack
			print(f'[{self.name}] Critical Attack {cri_attack} DMG')
		else:
			foe.health = foe.health - self.attack
			print(f'[{self.name}] Attack {self.attack} DMG')


class Human(Character):
	def __init__(self, newname):
		self.health = 100
		self.attack = 10
		self.name = newname

	# def doAttack(self, foe):
	# 	print(f'[{self.name}] Attack {self.attack} DMG')
	# 	super().doAttack(foe)
		


class Monster(Character):
	def __init__(self, newname=''):
		self.health = 100
		self.attack = 10
		self.name = newname

	# def doAttack(self, foe):
	# 	print(f'[{self.name}] Attack {self.attack} DMG')
	# 	super().doAttack(foe)

 		 

# Main Program
jack = Human("Jack the Hero")
wolf = Monster()

print('Game Start!')
counter = 0
while not jack.isDead() and not wolf.isDead():
	counter = counter + 1
	print(f'TURN: {counter}')
	wolf.showStat()
	jack.showStat()
	jack.doAttack(wolf)
	wolf.doAttack(jack)
	print('-'*15)
if jack.isDead():
	print('RIP, Human Die')
else:
	print('Yeah! Human Win')








