import pygame
from .app import screen
from .events import close
from .player import player
from .app import timer, FPS
from .map import map
from .music import music
from .font import bottle_font

def run():
    game = True
    music.start_music()
    while game:
        events = pygame.event.get()
        for event in events:
            if close(event= event):
                game = False
        screen.fill((255, 123, 255))
        map.blit_map(screen= screen, move= player.move_map())
        layer_list = map.collision_map()

        map.bottle_remove(player_hitbox= player.HITBOX)
        text = bottle_font.render(f"Bottles: {map.BOTTLE_COUNTER}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

        # map.collision_draw(screen= screen)
        player.can_move_right(layer_list)
        player.can_move_left(layer_list)
        player.show_image(screen= screen)
        player.gravity()
        player.player_move()
        # player.draw_hitbox(screen= screen)
        player.can_move_down(layer_list)
        player.jump()
        player.can_move_up(layer_list)
        timer.tick(FPS)
        pygame.display.flip()