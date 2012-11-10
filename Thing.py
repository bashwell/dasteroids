### Thing ###
#All tangible 'things' (ships, shots, etc.) are subclasses of Thing

import numpy as np 
from math import atan
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
        self.position += self.speed #using numpy vectors instead
        
    def draw(self, surface):
        #I don't think this ever gets called - BAA
        # It's just a prototype so that subclasses don't need to implement it, like
        # the other think/tick/etc functions.  Maybe it would be better to have each
        # object *need* to implement this one.
        "Each thing should look different"
        pass

    def donutVector(self, target):  #returns the shortest vector to the target
        flatXDist=self.position[0]-target.position[0]
        flatYDist=self.position[1]-target.position[1]
        
        donutXDist=self.position[0]-(target.position[0]+self.state.screenSize[0])
        donutYDist=self.position[1]-(target.position[1]+self.state.screenSize[1])

        return np.array([min(abs(flatXDist),abs(donutXDist)),min(abs(flatYDist),abs(donutYDist))])

    def donutHeading(self, target): #returns the heading to target in radians, -pi to pi
        headingVector = self.donutVector(target)
        return atan(headingVector[0]/headingVector[1])
        
    def absDistance(self, target):
        headingVector=self.donutVector(target)
        return np.sqrt(headingVector.dot(headingVector))     