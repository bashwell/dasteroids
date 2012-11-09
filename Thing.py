### Thing ###
#All tangible 'things' (ships, shots, etc.) are subclasses of Thing

import numpy as np 
class Thing(object):

    def __init__(self, state):
        self.state = state 
        #create numpy vectors
        self.speed = np.zeros(2)
        self.position = np.zeros(2)
        self.direction = 0

    def think(self):
        pass

    def collision(self, other):
        "Hit a thing, what now?"

    def tick(self):
        #self.position[0] += self.speed[0]
        #self.position[1] += self.speed[1]
        self.position+=self.speed #using numpy vectors instead
        
    def draw(self, surface):
        #I don't think this ever gets called - BAA
        "Each thing should look different"
        pass
