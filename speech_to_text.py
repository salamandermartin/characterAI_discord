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

    def speechtotext_from_mic(self):
        self.azure_audioconfig = speechsdk.audio.AudioConfig(use_default_microphone= True)
        self.azure_speechrecognizer = speechsdk.SpeechRecognizer(speech_config=self.azure_speechconfig, audio_config=self.azure_audioconfig)

        speech_recognition_result = self.azure_speechrecognizer.recognize_once_async().get()
        text_result = speech_recognition_result.text