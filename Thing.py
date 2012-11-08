import numpy as np
class Thing(object):

    def __init__(self, state):
        self.state = state
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
        self.position+=self.speed
        
    def draw(self, surface):
        "Each thing should look different"
        pass
