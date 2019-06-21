from random import random

class Human():
	def __init__(self):
		self.health = 100
		self.attack = 10

	def showstat(self):
		# print(name.upper())
		print(f'Human Health = {self.health}')
		# print(f'Human Attack = {self.attack}')

	def isDead(self):
		if self.health <= 0:
			return True
		else:
			return False

	def doAttack(self, opponent):
		opponent.health = opponent.health - self.attack
		print(f'Attackkk ! ({self.attack})')

	def doCriticalAttack(self):
		x = random()
		if x >= 0.5:
			print('Human Power UP')
			self.attack = self.attack*2


class Monster():
	def __init__(self):
		self.health = 500
		self.attack = 10

	def showhealth(self):
		print(f'Monster Health = {self.health}')

	def doAttack(self, opponent):
		opponent.health = opponent.health - self.attack
		print(f'WOOOOWOWS ! ({self.attack})')

	def isDead(self):
		if self.health <= 0:
			return True
		else:
			return False


# Main Program

jack = Human()
# print(jack.health)
# jack.showstat('jack the hero')
wolf = Monster()


print('Game Start!')
counter = 0
while not jack.isDead() and not wolf.isDead():
	counter = counter + 1
	print(f'TURN: {counter}')
	wolf.showhealth()
	jack.showstat()
	jack.doCriticalAttack()
	jack.doAttack(wolf)
	wolf.doAttack(jack)
	print('-'*15)
if jack.isDead():
	print('RIP, Human Die')
else:
	print('Yeah! Human Win')





