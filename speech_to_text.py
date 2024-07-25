import time
import keyboard
import os

class SpeechToTextManager:
    azure_speechconfig = None
    azure_audioconfig = None
    azure_speechrecognizer = None

    def __init__(self):
        try:
            self.azure_speechconfig = speechsdk.SpeechConfig(subscription=os.getenv('AZURE_TTS_KEY'), region = os.getenv('AZURE_TTS_REGION'))
        except TypeError:
            exit('No environment variables found for AZURE_TTS')

        self.azure_speechconfig.speech_recognition_language = "en-US"