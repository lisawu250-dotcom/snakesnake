import pygame, random, sys

pygame.init()
w, h, s = 400, 400, 20
screen= pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

snake = [(100, 100),(80,100), (60,100)]
food = (random.randrange(0, w, s), random.randrange(0, h, s))
direction = (s,0)
score = 0

while true:
