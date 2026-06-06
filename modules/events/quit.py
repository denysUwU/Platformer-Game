import pygame


def close(event):
    if event.type == pygame.QUIT:
        return True