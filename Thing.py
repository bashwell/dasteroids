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
        self.ID=self.state.maxIDNumber
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

    def donutDistance(self, target): #shortest distance to target in donut math
        flatVector=self.position-target.position
        distanceFlat=np.sqrt(flatVector.dot(flatVector))
        
        transposedPosition=[target.position[0]-self.state.screenSize[0], target.position[1]-self.state.screenSize[1]]
        donutVector=self.position-transposedPosition
        distanceDonut=np.sqrt(donutVector.dot(donutVector))
        
        return min(distanceFlat, distanceDonut)