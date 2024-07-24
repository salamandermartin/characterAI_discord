import time
import os
import asyncio
import soundfile as sf
from mutagen.mp3 import MP3
import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init(frequency=48000, buffer = 1024)

    def audio_play(self, file_path, sleep_during_playback = True, delete_file = False, play_using_music = True):
        if not pygame.mixer.get_init():
            pygame.mixer.init(frequency=48000, buffer = 1024)
