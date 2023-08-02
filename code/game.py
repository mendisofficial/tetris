from settings import *

class Game:
    def __init__(self):
        # general
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.dispaly_surface = pygame.display.get_surface()

    def run(self):
        self.dispaly_surface.blit(self.surface, (PADDING, PADDING))