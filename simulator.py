import pygame
from State import State
# Remove after testing
from Ship import Ship

size = [800, 600]

def main(argv):
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Dasteroids")

    clock = pygame.time.Clock()
    state = State(screen) #create the game state, give it the screen we just made

    done = False

    testInit(state)

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

                
        screen.fill((0, 0, 0)) # Black background

        # Think
        state.think() 

        # Tick (Move, change state, etc)
        state.tick()

        # Draw things
        state.draw()

        # Update Display
        pygame.display.flip()

        # 20 FPS
        clock.tick(20)

    pygame.quit()


def testInit(state):
    ship1 = Ship(state, position=[100, 200])
    ship2 = Ship(state, position=[500, 300])
    map(state.addThing, [ship1, ship2])

main([])
