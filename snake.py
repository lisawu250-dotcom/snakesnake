import pygame
import random
import sys

#some comments

def main():
    pygame.init()
    w, h, s = 400, 400, 20 # width, height, and size
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()

    snake = [(100, 100), (80, 100), (60, 100)]
    food = (random.randrange(0, w, s), random.randrange(0, h, s))
    direction = (s, 0)
    score = 0

    paused = False
    game_over = False

    font = pygame.font.Font(None, 36)

    def place_food():
        # ensure food is not placed on the snake
        while True:
            f = (random.randrange(0, w, s), random.randrange(0, h, s))
            if f not in snake:
                return f

    food = place_food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_r and game_over:
                    # restart the game
                    snake[:] = [(100, 100), (80, 100), (60, 100)]
                    direction = (s, 0)
                    score = 0
                    food = place_food()
                    game_over = False
                if not paused and not game_over:
                    if event.key == pygame.K_UP and direction != (0, s):
                        direction = (0, -s)
                    elif event.key == pygame.K_DOWN and direction != (0, -s):
                        direction = (0, s)
                    elif event.key == pygame.K_LEFT and direction != (s, 0):
                        direction = (-s, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-s, 0):
                        direction = (s, 0)

        if not paused and not game_over:
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
            snake.insert(0, new_head)

            if new_head == food:
                score += 1
                food = place_food()
            else:
                snake.pop()

            if (
                new_head[0] < 0
                or new_head[0] >= w
                or new_head[1] < 0
                or new_head[1] >= h
                or new_head in snake[1:]
            ):
                game_over = True

        # Clear screen every frame
        screen.fill((0, 0, 0))

        # Draw the snake and food
        for segment in snake:
            pygame.draw.rect(
                screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], s, s)
            )
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food[0], food[1], s, s))

        # HUD: score and pause/game-over messages
        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))

        if paused:
            pause_surf = font.render("PAUSED - press P to resume", True, (255, 255, 0))
            screen.blit(pause_surf, (w // 2 - pause_surf.get_width() // 2, h // 2))

        if game_over:
            go_surf = font.render(f"GAME OVER - Score: {score}", True, (255, 0, 0))
            restart_surf = font.render("Press R to restart", True, (255, 255, 255))
            screen.blit(go_surf, (w // 2 - go_surf.get_width() // 2, h // 2 - 20))
            screen.blit(restart_surf, (w // 2 - restart_surf.get_width() // 2, h // 2 + 20))

        pygame.display.flip()
        clock.tick(10)


if __name__ == "__main__":
    main()