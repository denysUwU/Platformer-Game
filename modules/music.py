import pygame
from .create_path import create_path

pygame.init()

class Music:
    def __init__(self, music_volume: int, music_repeat: int, music_name: str):
        self.MUSIC_VOLUME = music_volume
        self.MUSIC_REPEAT = music_repeat
        self.MUSIC_NAME = music_name
        self.load_music()
    def load_music(self):
        self.MUSIC_PATH = create_path(img = self.MUSIC_NAME, folder = "audio")
        pygame.mixer.music.load(self.MUSIC_PATH)
        pygame.mixer.music.set_volume(self.MUSIC_VOLUME)
    def unload_music(self):
        pygame.mixer.music.unload()
    def start_music(self):
        pygame.mixer.music.play(loops= self.MUSIC_REPEAT)
    def stop_music(self):
        pygame.mixer.music.stop()

music = Music(music_volume= 0.01, music_repeat= -1, music_name= "time_for_adventure.mp3")