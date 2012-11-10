### Thing ###
#All tangible 'things' (ships, shots, etc.) are subclasses of Thing

import numpy as np 
from math import atan, pi
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
        "Each thing should look different"
        pass

    def donutVector(self, target):  #returns the shortest vector to the target
        flatXDist = self.position[0]-target.position[0]
        flatYDist = self.position[1]-target.position[1]
        
        donutXDist = self.position[0]-(target.position[0]+self.state.screenSize[0])
        donutYDist = self.position[1]-(target.position[1]+self.state.screenSize[1])
         
        if ( abs(flatXDist) < abs(donutXDist) ):
            shortestX = flatXDist
            print "Flat X"
        else:
            shortestX=donutXDist   
            print "Donut X"
        if ( abs(flatYDist) < abs(donutYDist) ):
            shortestY = flatYDist
            print "Flat Y"
        else:
            print "Donut Y"
            shortestY=donutYDist   
        return np.array( [shortestX, shortestY] )    
        #return np.array([ min(abs(flatXDist), abs(donutXDist)), min(abs(flatYDist), abs(donutYDist)) ])


    def donutHeading(self, target): #returns the heading to target in radians, -pi to pi
        headingVector = self.donutVector(target)
        return atan(headingVector[0]/headingVector[1])
        
        
    def absDistance(self, target):
        headingVector=self.donutVector(target)
        return np.sqrt(headingVector.dot(headingVector))     