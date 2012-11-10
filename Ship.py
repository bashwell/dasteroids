from Thing import Thing
from Shot import Shot
import warnings
from drawUtils import drawPolygon, drawLine
from math import cos, sin

class Ship(Thing):
    
    def __init__(self, state, position=[0,0]):
        super(Ship, self).__init__(state)

        self.position = position

        self.size = 50  # px
        self.health = 100;
        self.turnSpeed = .2 # Rad/sec
        self.maxAcceleration = 2 # px/sec
        self.fireRate = 1000
        self.fireTimer = 0


    def think(self):
        "Brain goes here"
        if self.canFire():
            self.fire()

        self.turn(self.turnSpeed)
        self.accelerate(0.5 * self.maxAcceleration)
       

    def tick(self):
        if not self.fireTimer == 0:
            self.fireTimer -= 1
        super(Ship, self).tick()
       

    def draw(self):
        drawPolygon(self, [[-10, -10], [10, -10], [0, 15]])
        if (self.ID == 0):
            drawLine(self, self.position, [self.position[0], self.position[1]], self.donutHeading(self.state.listOfThings[1]))
        if (self.ID == 1):
            drawLine(self, [0,0], [100,0], self.donutHeading(self.state.listOfThings[0]))

    def collision(self, other):
        "I have hit a thing, how does that affect me?"
        pass

    ## State Changers

    def accelerate(self, delV):
        if delV > 0 and delV < self.maxAcceleration:
            self.speed[0] += cos(self.direction) * delV
            self.speed[1] += sin(self.direction) * delV
        else:
            warnings.warn("Ship cannot accelerate that fast", Warning)


    def turn(self, delTheta):
        "Turns ship by a change of delTheta, if it's able"
        if abs(delTheta) <= self.turnSpeed:
            self.direction += delTheta
        else:
            warnings.warn("Ship cannot turn that fast", Warning)


    def fire(self):
        if self.canFire():
            self.fireTimer = self.fireRate
            shot = Shot(self.state, self)
            self.state.addThing(shot)
    ## Predicates


    def canFire(self):
        return self.fireTimer == 0
        
    
