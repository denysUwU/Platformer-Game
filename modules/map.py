import pygame
import pytmx
from .create_path import create_path


class Map:
    def __init__(self, map_name: str):
        self.TILE_MAP = pytmx.load_pygame(create_path(img= map_name, folder= "tilemap"))
        self.TILE_HEIGHT = self.TILE_MAP.tileheight
        self.TILE_WIDTH = self.TILE_MAP.tilewidth
        self.BOTTLE_COUNTER = 0
        self.MOVE_MAP = 0

    def blit_map(self, screen: pygame.Surface, move):
        self.FULL_TILES = self.TILE_MAP.visible_tile_layers
        for layer_id in self.FULL_TILES:
            tiled_id = self.TILE_MAP.layers[layer_id]
            for x, y, cell_number in tiled_id:
                self.MOVE_MAP = move
                if cell_number != 0:
                    cell_image = self.TILE_MAP.get_tile_image_by_gid(
                        cell_number
                    )
                    screen.blit(cell_image, 
                                (x * self.TILE_WIDTH - self.MOVE_MAP , y * self.TILE_HEIGHT)
                                )
    def collision_map(self):
        rect_list = []
        self.MAP_COLLISION = self.TILE_MAP.get_layer_by_name(name= "collision")
        for layer in self.MAP_COLLISION:
            rect = pygame.Rect(layer.x - self.MOVE_MAP, layer.y, layer.width, layer.height)
            rect_list.append(rect)
        return rect_list
    def collision_draw(self, screen: pygame.Surface):
        self.DRAW_MAP_COLLISION = self.TILE_MAP.get_layer_by_name(name= "collision")
        for layer in self.DRAW_MAP_COLLISION:
            rect_map = pygame.Rect(layer.x - self.MOVE_MAP, layer.y, layer.width, layer.height)
            pygame.draw.rect(
                screen,
                color= (0, 0, 0),
                rect= rect_map,
                width= 3
            )
    def bottle_remove(self, player_hitbox: pygame.Rect):
        self.LAYER_BOTTLE = self.TILE_MAP.get_layer_by_name(name= "bottles")
        for y, row in enumerate(self.LAYER_BOTTLE.data):
            for x, cell in enumerate(row):
                if cell != 0:
                    rect = pygame.Rect(x * self.TILE_WIDTH - self.MOVE_MAP, y * self.TILE_HEIGHT, self.TILE_WIDTH, self.TILE_HEIGHT)
                    if player_hitbox.colliderect(rect):
                        self.LAYER_BOTTLE.data[y][x] = 0
                        self.BOTTLE_COUNTER += 1



map = Map(map_name= "map.tmx")
