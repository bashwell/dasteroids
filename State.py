from math import fmod

### State ###
# This is the 'state' of the game, and there is only one of these objects in play at a time


class State(object):

    def __init__(self, screen):
        self.screen = screen # the screen the game is playing on
        self.screenSize = screen.get_size()
        self.listOfThings = []
        self.maxIDNumber=0

    def addThing(self, thing):
        self.listOfThings.append(thing)
        thing.ID=self.maxIDNumber
        self.maxIDNumber+=1
        
    def removeThing(self, thing):
        self.listOfThings.remove(thing)

    def tick(self): #make everything tick
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

    def draw(self): #make everything draw
        for thing in self.listOfThings:
            thing.draw()

    def think(self): #make everything think
        for thing in self.listOfThings:
            thing.think()
        
        
