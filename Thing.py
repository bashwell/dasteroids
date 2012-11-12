### Thing ###
#All tangible 'things' (ships, shots, etc.) are subclasses of Thing

import numpy as np 
from math import atan2, pi
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
        
        if (abs(flatXDist) < 0.5*self.state.screenSize[0]): #it's shorter in the flat dimension
            shortestX=flatXDist
        elif (flatXDist > 0):
            shortestX= flatXDist-self.state.screenSize[0]  
        else:
            shortestX= flatXDist+self.state.screenSize[0]  
        
        if (abs(flatYDist) < 0.5*self.state.screenSize[1]): #it's shorter in the flat dimension
            shortestY=flatYDist
        elif (flatYDist > 0):
            shortestY= flatYDist-self.state.screenSize[1]  
        else:
            shortestY= flatYDist+self.state.screenSize[1]  
       
      
        return np.array( [shortestX, shortestY] )    
      
    def donutHeading(self, target): #returns the heading to target in radians, -pi to pi
        headingVector = self.donutVector(target)
        return atan2(headingVector[1],headingVector[0])
        
        
    def absDistance(self, target):
        headingVector=self.donutVector(target)
        return np.sqrt(headingVector.dot(headingVector))     