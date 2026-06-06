import pygame
from .create_path import create_path

class Settings:
    def __init__(self, width: int, height: int, name_image: str, coordinate_x: int, coordinate_y: int):
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME_IMAGE = name_image
        self.COORDINATE_X = coordinate_x
        self.COORDINATE_Y = coordinate_y
        self.load_image()
    def load_image(self, direction_x = False):
        self.IMAGE = pygame.image.load(create_path(self.NAME_IMAGE, "media"))
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
        self.IMAGE = pygame.transform.flip(self.IMAGE, direction_x, False)
    def show_image(self, screen: pygame.Surface):
        screen.blit(self.IMAGE, (self.COORDINATE_X, self.COORDINATE_Y))
        
