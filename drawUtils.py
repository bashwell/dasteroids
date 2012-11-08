import pygame
from math import sin, cos

drawWidth = 2
drawColor = [255, 255, 255] # white

def relativeToAbsolute(thing, points):
    return map(lambda point: (thing.position[0] + point[0], thing.position[1] + point[1]), points)

def rotatePoint(direction, point):
    x = point[0] * cos(direction) - point[1] * sin(direction)

    y = point[0] * sin(direction) + point[1] * cos(direction)

    return [x, y]

def rotatePointsByThing(thing, points):
    return map(lambda point: rotatePoint(thing.direction, point),
               points)

def thingToScreen(thing, points):
    return relativeToAbsolute(thing, rotatePointsByThing(thing, points))

def drawPolygon(thing, points):
    # Translate points from relative to the ship to the globabl screen coordinates
    points = thingToScreen(thing, points)

    pygame.draw.polygon(thing.state.screen, drawColor, points, drawWidth)

def drawCircle(thing, center, radius):
    center[0] += thing.position[0]
    center[1] += thing.position[1]

    pygame.draw.circle(thing.state.screen, drawColor, [int(n) for n in center], radius, drawWidth)
