from Thing import Thing
from drawUtils import drawCircle
from math import sin, cos

class Shot(Thing):

    def __init__(self, state, parent):
        super(Shot, self).__init__(state)

        self.position = parent.position[:]
        self.direction = parent.direction
        self.speed[0] = 10 * cos(parent.direction)
        self.speed[1] = 10 * sin(parent.direction)
        self.lifeClock = 0;


    def collision(self, thing):
        self.state.removeThing(self)

    def draw(self):
        drawCircle(self, [0, 0], 10)

    def think(self):
        pass

    def tick(self):
        self.lifeClock +=1
        super(Shot, self).tick()
        
        # print 'Shot at ({}, {}) with speed ({}, {})'.format(self.position[0], self.position[1], self.speed[0], self.speed[1])

        if (self.lifeClock > 200):
            self.state.removeThing(self)
