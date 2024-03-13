import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Definição de constantes
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Configuração da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Classe para representar a cobra
class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def move(self):
        head = self.body[0]
        x, y = head

        if self.direction == 'UP':
            y -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            y += BLOCK_SIZE
        elif self.direction == 'LEFT':
            x -= BLOCK_SIZE
        elif self.direction == 'RIGHT':
            x += BLOCK_SIZE

        self.body.insert(0, (x, y))

    def grow(self):
        tail = self.body[-1]
        x, y = tail

        if self.direction == 'UP':
            y += BLOCK_SIZE
        elif self.direction == 'DOWN':
            y -= BLOCK_SIZE
        elif self.direction == 'LEFT':
            x += BLOCK_SIZE
        elif self.direction == 'RIGHT':
            x -= BLOCK_SIZE

        self.body.append((x, y))

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

# Classe para representar a maçã
class Apple:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - BLOCK_SIZE)
        self.y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE)

    def respawn(self):
        self.x = random.randint(0, SCREEN_WIDTH - BLOCK_SIZE)
        self.y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

# Função para reiniciar o jogo
def restart():
    snake.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    snake.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
    apple.respawn()

# Instância da cobra e da maçã
snake = Snake()
apple = Apple()

# Loop principal do jogo
running = True
while running:
    screen.fill(BLACK)

    # Manipulação de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != 'DOWN':
                snake.direction = 'UP'
            elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                snake.direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                snake.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                snake.direction = 'RIGHT'

    # Verifica se a cobra colidiu com a maçã
    head_x, head_y = snake.body[0]
    apple_x, apple_y = apple.x, apple.y
    if abs(head_x - apple_x) < BLOCK_SIZE and abs(head_y - apple_y) < BLOCK_SIZE:
        snake.grow()
        apple.respawn()

    # Verifica se a cobra colidiu com as bordas
    if (snake.body[0][0] < 0 or snake.body[0][0] >= SCREEN_WIDTH or
        snake.body[0][1] < 0 or snake.body[0][1] >= SCREEN_HEIGHT):
        restart()

    # Verifica se a cobra colidiu com seu próprio corpo
    if snake.body[0] in snake.body[1:]:
        restart()

    # Movimento da cobra
    snake.move()

    # Desenho da cobra e da maçã
    snake.draw()
    apple.draw()

    pygame.display.update()
    clock.tick(10)

pygame.quit()
sys.exit()
