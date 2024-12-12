import pygame
import time
import math
import random

# Initialize Pygame
pygame.init()

# Constants for game setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
SIDEBAR_WIDTH = 200

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Base Game Class
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH + SIDEBAR_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Strategy Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.gold = 50
        self.points = 0
        self.total_points = 0
        self.wave = 1
        self.next_wave_threshholds = [50, 100, 500, 1000]
        self.core = Core(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.objects = []
        self.zombies = []
        self.spawn_timer = 0
        self.start_time = time.time()
        self.game_time = 0
        self.in_prep_time = True
        self.prep_start_time = time.time()
        self.state = "start"  # Possible states: start, playing, game_over, game_completed
        self.mouse_clicked = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            if self.state == "start":
                self.show_start_screen()
            elif self.state == "playing":
                if self.in_prep_time:
                    self.handle_prep_time()
                else:
                    self.game_time = time.time() - self.start_time
                    self.update()
                self.draw()
            elif self.state == "game_over":
                self.show_game_over_screen()
            elif self.state == "game_completed":
                self.show_game_completed_screen()
            pygame.display.flip()

    def show_start_screen(self):
        self.screen.fill(BLACK)
        font = pygame.font.Font(None, 74)
        text = font.render("Strategy Game", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
        font = pygame.font.Font(None, 36)
        text = font.render("Press ENTER to Start", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.state = "playing"
            self.start_time = time.time()

    def show_game_over_screen(self):
        self.screen.fill(BLACK)
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, RED)
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
        font = pygame.font.Font(None, 36)
        text = font.render("Press R to Restart", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.__init__()
            self.state = "playing"

    def show_game_completed_screen(self):
        self.screen.fill(BLACK)
        font = pygame.font.Font(None, 74)
        text = font.render("Game Completed", True, GREEN)
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
        font = pygame.font.Font(None, 36)
        text = font.render("Press R to Restart", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.__init__()
            self.state = "playing"

    def handle_prep_time(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.in_prep_time = False
            self.start_time = time.time()
        self.buy_object_place()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_clicked = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_clicked = False
        if self.state == "playing":
            self.core.update()
            for obj in self.objects:
                obj.update()
            for zombie in self.zombies:
                zombie.update()

            if not self.in_prep_time:
                # damage periodically
                self.damage()

                # Spawn Zombies periodically
                self.spawn_timer += 1
                spawn_interval = max(30, 180 - self.wave * 10 - int(self.game_time // 60) * 5)  # Adjust spawn frequency based on wave and game time
                if self.spawn_timer >= spawn_interval:
                    self.spawn_timer = 0
                    for i in range(self.wave):
                        x = random.choice([0, SCREEN_WIDTH])
                        y = random.randint(0, SCREEN_HEIGHT)
                        self.zombies.append(Zombie(x, y, self.wave))  # Spawn leveled-up enemies

            # Allow object placement even after prep time
            self.buy_object_place()
            self.level_up_objects()

    def update(self):
        # Update game state
        self.core.update()
        for obj in self.objects:
            obj.update()
        for zombie in self.zombies:
            zombie.update()
        self.damage()
        if self.core.hp <= 0:
            self.state = "game_over"
        if self.total_points >= 200:  # Show game completed when points reach 200
            self.state = "game_completed"
        self.points = self.total_points
        if game.game_time >= 60:
            self.next_wave()

    def draw(self):
        self.screen.fill(WHITE)
        self.core.draw(self.screen)
        for obj in self.objects:
            obj.draw(self.screen)
        for zombie in self.zombies:
            zombie.draw(self.screen)
        self.draw_sidebar()
        pygame.display.flip()
    
    def draw_sidebar(self):
        pygame.draw.rect(self.screen, BLACK, (SCREEN_WIDTH, 0, SIDEBAR_WIDTH, SCREEN_HEIGHT))
        font = pygame.font.Font(None, 36)
        text = font.render(f"Gold: {self.gold}", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH + 10, 10))
        text = font.render(f"Points: {self.points}", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH + 10, 50))
        text = font.render("Keys:", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH + 10, 90))
        text = font.render("1: Torrent (5 Gold)", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH + 10, 130))
        text = font.render("2: Wall (1 Gold)", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH + 10, 170))
        text = font.render("3: Electric Tower (10 Gold)", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH + 10, 210))
        text = font.render("4: Trap", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH + 10, 250))
        text = font.render("5: Mine (5 Points)", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH + 10, 290))
        text = font.render(f"Game Time: {int(self.game_time)}", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH + 10, 330))

    def buy_object_place(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        if mouse_x > SCREEN_WIDTH:
            return

        if mouse_buttons[0] and self.mouse_clicked:  # Left mouse button is pressed and not already clicked
            if keys[pygame.K_1] and self.gold >= 5:
                self.objects.append(Torrent(mouse_x, mouse_y, 100))
                self.gold -= 5
            elif keys[pygame.K_2] and self.gold >= 1:
                self.objects.append(Wall(mouse_x, mouse_y))
                self.gold -= 1
            elif keys[pygame.K_3] and self.gold >= 10:
                self.objects.append(ElectricTower(mouse_x, mouse_y))
                self.gold -= 10
            elif keys[pygame.K_4] and self.gold >= 3:
                self.objects.append(Trap(mouse_x, mouse_y))
                self.gold -= 3
            elif keys[pygame.K_5] and self.points >= 5:
                self.objects.append(Mine(mouse_x, mouse_y))
                self.points -= 5
            elif keys[pygame.K_5] and self.points >= 5:
                self.objects.append(Mine(mouse_x, mouse_y))
                self.points -= 5
            self.mouse_clicked = False  # Reset mouse click 
            
    
    def level_up_objects(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        if mouse_buttons[0] and self.mouse_clicked and keys[pygame.K_l]:  # Left mouse button and 'L' key pressed
            for obj in self.objects:
                if isinstance(obj, (Torrent, Wall, ElectricTower, Trap, Mine)) and math.hypot(obj.x - mouse_x, obj.y - mouse_y) < 20 and self.gold >= obj.level:
                    self.gold -= obj.level
                    obj.level_up()
                    self.mouse_clicked = False  # Reset mouse click state

    def next_wave(self):
        lis = self.next_wave_threshholds
        for i in range(len(lis)):
            if lis[i] <= self.total_points:
                self.wave = i + 1
        self.in_prep_time = True
        self.prep_start_time = time.time()
        self.spawn_timer = max(30, 180 - self.wave * 10 - int(self.game_time // 60) * 5)  # Increase spawn frequency
    
    def damage(self):
        # Check if torrent's bullets are colliding with enemy or our things (nullify in this case)
        for obj in self.objects:
            if isinstance(obj, Bullet):
                for zombie in self.zombies:
                    if math.hypot(obj.x - zombie.x, obj.y - zombie.y) < 10:
                        zombie.hp -= obj.damage
                        self.objects.remove(obj)
                        if zombie.hp <= 0:
                            self.zombies.remove(zombie)
                            self.total_points += 10
                        break
                for other_obj in self.objects:
                    if other_obj != obj and math.hypot(obj.x - other_obj.x, obj.y - other_obj.y) < 10:
                        if not isinstance(other_obj, Trap):
                            self.objects.remove(obj)
                        break

        # Check if electric tower has enemies in its range and time_between_atk has passed
        for obj in self.objects:
            if isinstance(obj, ElectricTower):
                current_time = time.time()
                if current_time - obj.last_atk_time >= obj.time_between_atks:
                    for zombie in self.zombies:
                        if math.hypot(obj.x - zombie.x, obj.y - zombie.y) <= obj.range:
                            zombie.hp -= obj.damage
                            if zombie.hp <= 0:
                                self.zombies.remove(zombie)
                                self.total_points += 10
                    obj.last_atk_time = current_time

        # Check if zombies are colliding with core, mines, or other objects
        for zombie in self.zombies:
            if math.hypot(zombie.x - self.core.x, zombie.y - self.core.y) < self.core.radius:
                self.core.hp -= zombie.damage
                if self.core.hp <= 0:
                    self.state = "game_over"
            for obj in self.objects:
                if isinstance(obj, (Mine, Wall, Torrent, ElectricTower)) and math.hypot(zombie.x - obj.x, zombie.y - obj.y) < 20:
                    obj.hp -= zombie.damage
                    if obj.hp <= 0:
                        self.objects.remove(obj)
                elif isinstance(obj, Trap) and math.hypot(zombie.x - obj.x, obj.y - obj.y) < 20:
                    zombie.hp -= obj.damage
                    if zombie.hp <= 0:
                        self.zombies.remove(zombie)
                        self.total_points += 10
                    self.objects.remove(obj)
                elif isinstance(obj, ElectricTower) and math.hypot(zombie.x - obj.x, zombie.y - obj.y) <= obj.range:
                    zombie.hp -= obj.damage
                    if zombie.hp <= 0:
                        self.zombies.remove(zombie)
                        self.total_points += 10

# Core Class
class Core:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 5000
        self.radius = 40

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius)
        font = pygame.font.Font(None, 24)
        text = font.render(f"HP: {self.hp}", True, BLACK)
        screen.blit(text, (self.x - 20, self.y - 10))

# Base Object Class
class GameObject:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp

    def update(self):
        pass

    def draw(self, screen):
        pass

# Bullet Class
class Bullet(GameObject):
    def __init__(self, x, y, target, speed, damage):
        super().__init__(x, y, 1)
        self.target = target
        self.speed = speed
        self.damage = damage

    def update(self):
        direction = math.atan2(self.target.y - self.y, self.target.x - self.x)
        self.x += self.speed * math.cos(direction)
        self.y += self.speed * math.sin(direction)
        if math.hypot(self.x - self.target.x, self.y - self.target.y) < 10:
            self.target.hp -= self.damage
            if self.target.hp <= 0 and self.target in game.zombies:
                game.zombies.remove(self.target)
                game.total_points += 10

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), 5)

# Torrent Class
class Torrent(GameObject):
    def __init__(self, x, y, hp):
        super().__init__(x, y, hp)
        self.gold_cost = 5
        self.rate_of_fire = 1  # Shots per second
        self.damage = 10  # per bullet
        self.range = 300  # Increase range to 300 pixels
        self.level = 1
        self.last_shot_time = time.time()
        self.bullets_shot = []

    def update(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= 1 / self.rate_of_fire:
            self.shoot()
            self.last_shot_time = current_time

        for bullet in self.bullets_shot:
            bullet.update()
            if bullet not in game.objects:
                self.bullets_shot.remove(bullet)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 20, 20))
        for bullet in self.bullets_shot:
            bullet.draw(screen)
        font = pygame.font.Font(None, 24)
        text = font.render(f"HP: {self.hp}", True, BLACK)
        screen.blit(text, (self.x, self.y - 20))

    def shoot(self):
        for zombie in game.zombies:
            if math.hypot(self.x - zombie.x, self.y - zombie.y) <= self.range:
                bullet = Bullet(self.x, self.y, zombie, 5, self.damage)
                self.bullets_shot.append(bullet)
                game.objects.append(bullet)
                break

    def level_up(self):
        self.level += 1
        self.rate_of_fire = self.level
        self.damage += 10
        self.hp += self.level * 10

# Wall Class
class Wall(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 10)
        self.gold_cost = 1
        self.level = 1

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 20, 20))
        font = pygame.font.Font(None, 24)
        text = font.render(f"HP: {self.hp}", True, BLACK)
        screen.blit(text, (self.x, self.y - 20))

    def level_up(self):
        self.hp += self.level * 10

# Electric Tower Class
class ElectricTower(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 1000)
        self.gold_cost = 10
        self.level = 1
        self.range = 50  # pixels
        self.damage = 10  # all in range
        self.time_between_atks = 5
        self.last_atk_time = 0

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), 30)
        font = pygame.font.Font(None, 24)
        text = font.render(f"HP: {self.hp}", True, BLACK)
        screen.blit(text, (self.x - 20, self.y - 40))
    
    def level_up(self):
        self.level += 1
        self.hp += self.level * 10
        self.damage *= 2
        self.range += 20
        if self.time_between_atks > 1:
            self.time_between_atks -= 1
        
# Trap Class
class Trap(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 50)
        self.level = 1
        self.range = 5
        self.damage = 10
        self.gold_cost = 3  # Set the cost of traps to 3 gold

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, 20, 20))
        # Removed HP display for traps

    def level_up(self):
        self.level += 1
        self.hp += self.level * 10
        self.range += 2
        self.damage += 10

# Mine Class
class Mine(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 50)
        self.production_rate = 10  # number of seconds per Gold produced
        self.last_production_time = time.time()

    def update(self):
        current_time = time.time()
        if current_time - self.last_production_time >= self.production_rate:
            game.gold += 1
            self.last_production_time = current_time

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, (self.x, self.y, 20, 20))
        font = pygame.font.Font(None, 24)
        text = font.render(f"HP: {self.hp}", True, BLACK)
        screen.blit(text, (self.x, self.y - 20))
    
    def level_up(self):
        self.level += 1
        self.production_rate /= 2

# Enemies
# Base Zombie Class
class Zombie(GameObject):
    def __init__(self, x, y, level):
        super().__init__(x, y, 10)
        self.speed = 1  # Decrease speed to 1
        self.damage = 1
        self.level = level
        self.attack_rate = 1  # Constant attack rate for all levels
        for i in range(level):
            self.level_up()

    def update(self):
        # Move towards the core or nearest mine
        target = game.core
        for obj in game.objects:
            if isinstance(obj, Mine) and math.hypot(self.x - obj.x, self.y - obj.y) < 100:
                target = obj
                break
        direction = math.atan2(target.y - self.y, target.x - self.x)
        self.x += self.speed * math.cos(direction)
        self.y += self.speed * math.sin(direction)

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 10)
        font = pygame.font.Font(None, 24)
        text = font.render(f"HP: {self.hp}", True, BLACK)
        screen.blit(text, (self.x - 10, self.y - 20))

    def level_up(self):
        self.hp *= 10
        self.damage *= 5
        self.speed /= 2


# Create and run the game
game = Game()
game.run()

pygame.quit()