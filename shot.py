from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, position, direction):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = direction * PLAYER_SHOT_SPEED

    def update(self, dt):
        self.position += self.velocity * dt

        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), self.position, self.radius)
