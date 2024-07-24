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

        if play_using_music:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        else:
            pygame_sound = pygame.mixer.Sound(file_path)
            pygame_sound.play()

        if sleep_during_playback:
            _, ext = os.path.splittext(file_path)
            if ext.lower() == '.wav':
                wav_file = sf.SoundFile(file_path)
                file_length = wav_file.frames / wav_file.samplerate
                wav_file.close()
            elif ext.lower() == '.mp3':
                mp3_file = MP3(file_path)
                file_length = mp3_file.info.length
            else:
                return
            
            time.sleep(file_length)

            if delete_file:
                pygame.mixer.music.stop()
                pygame.mixer.quit()

                try:
                    os.remove(file_path)
                except PermissionError:
                    print(f"Couldn't remove {file_path} -- it is being used by another process")

    async def play_audio_async(self, file_path):
        if not pygame.mixer.get_init():
            pygame.mixer.init(frequency = 48000, buffer = 1024)
                    
