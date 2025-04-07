import pygame
import time
import random

# Настройки игры
snake_speed = 15
window_x = 720
window_y = 480

# Цвета
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)     # Еда 1 очко
yellow = pygame.Color(255, 255, 0) # Еда 2 очка
blue = pygame.Color(0, 0, 255)     # Еда 3 очка
green = pygame.Color(0, 255, 0)    # Змея

pygame.init()
pygame.display.set_caption('Змейка')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Параметры змеи
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Параметры еды
food_position = [random.randrange(1, (window_x // 10)) * 10,
                 random.randrange(1, (window_y // 10)) * 10]

food_weight = random.choice([1, 2, 3])  # Вес еды (очки за неё)
food_color = red if food_weight == 1 else yellow if food_weight == 2 else blue
food_timer = 0  # Таймер исчезновения еды
food_lifetime = 7 * snake_speed  # Через сколько тиков еда исчезнет

# Направление змеи
direction = 'RIGHT'
change_to = direction

score = 0

# Функция отображения счёта
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Функция окончания игры
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Основной цикл игры
while True:
    # Обработка событий управления
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Проверка невозможных поворотов
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Движение змеи
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Добавление новой головы
    snake_body.insert(0, list(snake_position))

    # Проверка съедения еды
    if snake_position == food_position:
        score += food_weight * 10  # Очки зависят от веса еды
        # Генерация новой еды
        food_position = [random.randrange(1, (window_x // 10)) * 10,
                         random.randrange(1, (window_y // 10)) * 10]
        food_weight = random.choice([1, 2, 3])
        food_color = red if food_weight == 1 else yellow if food_weight == 2 else blue
        food_timer = 0  # Сброс таймера еды
    else:
        snake_body.pop()

    # Обновление таймера еды
    food_timer += 1
    if food_timer > food_lifetime:
        food_position = [random.randrange(1, (window_x // 10)) * 10,
                         random.randrange(1, (window_y // 10)) * 10]
        food_weight = random.choice([1, 2, 3])
        food_color = red if food_weight == 1 else yellow if food_weight == 2 else blue
        food_timer = 0

    # Отображение змеи и еды
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, food_color, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Проверка столкновений
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # Отображение счёта
    show_score(white, 'times new roman', 20)

    # Обновление экрана
    pygame.display.update()
    fps.tick(snake_speed)