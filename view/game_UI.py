import pygame
from pygame.locals import *
import os
import random
from controllers.user import Player

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
FONT = pygame.font.Font(None, 36)

# Load assets
ASSETS_FOLDER = "C:/Users/skpar/OneDrive/Documents/GitHub/Misthos/assets"
PLAYER_IMAGES = {
    "Hero1": pygame.image.load(os.path.join(ASSETS_FOLDER, "hero1.png")),
    "Hero2": pygame.image.load(os.path.join(ASSETS_FOLDER, "hero2.png")),
    "Hero3": pygame.image.load(os.path.join(ASSETS_FOLDER, "hero3.png"))
}
ORC_IMAGE = pygame.image.load(os.path.join(ASSETS_FOLDER, "orc.png"))

# Player class
class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = PLAYER_IMAGES[player.user_name]
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 5
        if keys[K_RIGHT]:
            self.rect.x += 5
        if keys[K_UP]:
            self.rect.y -= 5
        if keys[K_DOWN]:
            self.rect.y += 5

# Orc class
class OrcSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = ORC_IMAGE
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Main game class
class RPGGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Story Mode RPG Game")
        self.clock = pygame.time.Clock()
        self.running = True

        # Create players
        self.players = [
            Player("Hero1", "avatar1.png", 10, 10, 10, 10, 100, {}),
            Player("Hero2", "avatar2.png", 12, 8, 10, 12, 100, {}),
            Player("Hero3", "avatar3.png", 8, 12, 12, 8, 100, {})
        ]
        self.player_sprites = pygame.sprite.Group([PlayerSprite(player) for player in self.players])
        self.all_sprites = pygame.sprite.Group(self.player_sprites)
        self.orcs = pygame.sprite.Group()

        # Spawn initial orcs
        self.spawn_orcs(5)

    def spawn_orcs(self, count):
        for _ in range(count):
            x = random.randint(0, SCREEN_WIDTH - 50)
            y = random.randint(0, SCREEN_HEIGHT - 50)
            orc = OrcSprite(x, y)
            self.orcs.add(orc)
            self.all_sprites.add(orc)

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()
        # Check for collisions between players and orcs
        if pygame.sprite.groupcollide(self.player_sprites, self.orcs, False, False):
            self.running = False  # End game on collision

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

# Main function
def main():
    game = RPGGame()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()