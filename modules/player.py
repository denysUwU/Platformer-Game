import pygame
from .settings import Settings
from .app import screen

class Player(Settings):
    def __init__(self, health: int, step: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.HEALTH = health
        self.STEP = step
        self.HITBOX = pygame.Rect(self.COORDINATE_X, self.COORDINATE_Y, self.WIDTH, self.HEIGHT)
        self.Y_VELOCITY = 0
        self.ON_GROUND = False
        self.CAN_MOVE_RIGHT = True
        self.CAN_MOVE_LEFT = True
        self.DIRECTION = "right"
        self.ANIMATION_SPEED = 0
        self.IMAGE_NUMBER = 0
        self.CURRENT_ANIMATION = "breath"
        self.MOVE_MAP_SPEED = 3
        self.MOVE_MAP_COUNTER = 0
        
    def draw_hitbox(self, screen: pygame.Surface):
        pygame.draw.rect(
            surface= screen,
            color= (0, 245, 155),
            rect= self.HITBOX,
            width= 3
        )

    def player_move(self):
        pressed_buttons = pygame.key.get_pressed()
        if pressed_buttons[pygame.K_RIGHT] and self.CAN_MOVE_RIGHT == True:
            self.COORDINATE_X += self.STEP
            self.HITBOX.x += self.STEP
            self.DIRECTION = "right"
            if self.CURRENT_ANIMATION != "run":
                self.IMAGE_NUMBER = 0
                self.CURRENT_ANIMATION = "run"
            self.animation(image_count= 6, folder_name= "run1")
        elif pressed_buttons[pygame.K_LEFT] and self.CAN_MOVE_LEFT == True:
            self.COORDINATE_X -= self.STEP
            self.HITBOX.x -= self.STEP
            self.DIRECTION = "left"
            if self.CURRENT_ANIMATION != "run":
                self.IMAGE_NUMBER = 0
                self.CURRENT_ANIMATION = "run"
            self.animation(image_count= 6, folder_name= "run1")
        else:
            if self.ON_GROUND == True:
                if self.CURRENT_ANIMATION != "breath":
                    self.IMAGE_NUMBER = 0
                    self.CURRENT_ANIMATION = "breath"
                self.animation(image_count= 11, folder_name= "breath")
        if self.COORDINATE_X <= 0:
            self.COORDINATE_X = 0
            self.HITBOX.x = self.COORDINATE_X
        if self.COORDINATE_X + self.WIDTH >= screen.get_width():
            self.COORDINATE_X = screen.get_width() - self.WIDTH
            self.HITBOX.x = self.COORDINATE_X
    def gravity(self):
        self.Y_VELOCITY += 1
        if self.Y_VELOCITY >= 10:
            self.Y_VELOCITY = 10
        self.COORDINATE_Y += self.Y_VELOCITY
        self.HITBOX.y += self.Y_VELOCITY
        if self.ON_GROUND == False:
            if self.Y_VELOCITY > 0:
                if self.CURRENT_ANIMATION != "breath":
                    self.IMAGE_NUMBER = 0
                    self.CURRENT_ANIMATION = "breath"
                self.animation(image_count= 11, folder_name= "breath")

    def can_move_down(self, blocks: list):
        for block in blocks:
            if self.HITBOX.y + self.HITBOX.height >= block.y and self.HITBOX.y < block.y:
                if self.HITBOX.x + self.HITBOX.width - 15 >= block.x and self.HITBOX.x +15 <= block.x + block.width:
                    self.Y_VELOCITY = 0
                    self.COORDINATE_Y = block.y - self.HEIGHT
                    self.HITBOX.y = block.y - self.HITBOX.height
                    self.ON_GROUND = True
                    break
    def jump(self):
        pressed_buttons = pygame.key.get_pressed()
        if pressed_buttons[pygame.K_UP] and self.ON_GROUND == True:
            self.Y_VELOCITY = -20
            self.ON_GROUND = False
            if self.CURRENT_ANIMATION != "jump":
                self.IMAGE_NUMBER = 0
                self.CURRENT_ANIMATION = "jump"
            self.animation(image_count= 2, folder_name= "jump")

    def can_move_right(self, block_list: list):
        for block in block_list:
            if self.HITBOX.y < block.y + block.height and self.HITBOX.y + self.HEIGHT > block.y:
                if self.HITBOX.x < block.x and self.HITBOX.x + self.WIDTH > block.x:
                    self.CAN_MOVE_RIGHT = False
                    break
                else:
                    self.CAN_MOVE_RIGHT = True
            else: 
                self.CAN_MOVE_RIGHT = True
    
    def can_move_left(self, block_list: list):
        for block in block_list:
            if self.HITBOX.y < block.y + block.height and self.HITBOX.y + self.HEIGHT > block.y:
                if self.HITBOX.x < block.x + block.width and self.HITBOX.x + self.WIDTH > block.x + block.width:
                    self.CAN_MOVE_LEFT = False
                    break
                else:
                    self.CAN_MOVE_LEFT = True
            else: 
                self.CAN_MOVE_LEFT = True

    def can_move_up(self, block_list: list):
        for block in block_list:
            if self.HITBOX.y < block.y + block.height and self.HITBOX.y + self.HITBOX.height > block.y:
                if self.HITBOX.x < block.x + block.width and self.HITBOX.x + self.HITBOX.width > block.x:
                    self.Y_VELOCITY = 0

    def direction_image(self):
        if self.DIRECTION == "right":
            self.load_image(direction_x= False)
        if self.DIRECTION == "left":
            self.load_image(direction_x= True)
    
    def animation(self, image_count, folder_name):
        self.ANIMATION_SPEED += 1
        if self.ANIMATION_SPEED % image_count == 0:
            self.IMAGE_NUMBER += 1
            if self.IMAGE_NUMBER >= image_count:
                self.IMAGE_NUMBER = 0
            self.NAME_IMAGE = f"{folder_name}/{self.IMAGE_NUMBER}.png"
            self.direction_image()
    def move_map(self):
        pressed_buttons = pygame.key.get_pressed()
        if pressed_buttons[pygame.K_RIGHT] and self.CAN_MOVE_RIGHT == True:
            if self.COORDINATE_X >= 600:
                self.MOVE_MAP_COUNTER += self.MOVE_MAP_SPEED
                if self.MOVE_MAP_COUNTER >= 999:
                    self.MOVE_MAP_COUNTER = 999
                    self.STEP = 3
                else:
                    self.STEP = 0
            else:
                self.STEP = 3
        elif pressed_buttons[pygame.K_LEFT] and self.CAN_MOVE_LEFT == True:
            self.MOVE_MAP_COUNTER -= self.MOVE_MAP_SPEED
            if self.MOVE_MAP_COUNTER <= 0:
                self.MOVE_MAP_COUNTER = 0
                self.STEP = 3
            else:
                self.STEP = 0
        return self.MOVE_MAP_COUNTER

player = Player(width= 80, height= 80, name_image= "player.png", coordinate_x = 0, coordinate_y = 0, health= 10, step= 3)
