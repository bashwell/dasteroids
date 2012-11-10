import pygame
import numpy
from math import sin, cos

drawWidth = 2
drawColor = [255, 255, 255] # white
drawColorRed = [255, 0, 0] # white

def relativeToAbsolute(thing, points):
    return map(lambda point: (thing.position[0] + point[0], thing.position[1] + point[1]), points)

def rotatePoint(direction, point): #rotates points around 0
    x = point[0] * cos(direction) - point[1] * sin(direction)

    y = point[0] * sin(direction) + point[1] * cos(direction)

    return [x, y]

def rotatePointsByThing(thing, points): #rotates a point around a relative center
    return map(lambda point: rotatePoint(thing.direction, point), points)

def thingToScreen(thing, points): #take point from reference frame of the ship to screen at large
    return relativeToAbsolute(thing, rotatePointsByThing(thing, points))

def drawPolygon(thing, points):
    # Translate points from relative to the ship to the globabl screen coordinates
    points = thingToScreen(thing, points)

    pygame.draw.polygon(thing.state.screen, drawColor, points, drawWidth)

def drawCircle(thing, center, radius):

    pygame.draw.circle(thing.state.screen, drawColor, center.astype(int), radius, drawWidth)

def drawLine(thing, start, end, direction):
    pygame.draw.line(thing.state.screen, drawColorRed, start, rotatePoint(direction, end))