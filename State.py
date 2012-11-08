from math import fmod

class State(object):

	def __init__(self, screen):
		self.screen = screen
		self.screenSize = screen.get_size()
		self.listOfThings = []


	def addThing(self, thing):
		self.listOfThings.append(thing)

	def removeThing(self, thing):
		self.listOfThings.remove(thing)

	def tick(self):
		for thing in self.listOfThings:
			thing.tick()

			# doughnut world!
			if thing.position[0] > self.screenSize[0]:
				thing.position[0] -= self.screenSize[0]
			elif thing.position[0] < 0:
				thing.position[0] += self.screenSize[0]

			if thing.position[1] > self.screenSize[1]:
				thing.position[1] -= self.screenSize[1]
			elif thing.position[1] < 0:
				thing.position[1] += self.screenSize[1]

			thing.direction = fmod(thing.direction, 2 * 3.14159)

	def draw(self):
		for thing in self.listOfThings:
			thing.draw()

	def think(self):
		for thing in self.listOfThings:
			thing.think()
		
		
