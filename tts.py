import pyttsx3
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide' 

try:
    engine = pyttsx3.init('sapi5')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 10)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 0.5)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
except ImportError:
    print('Requested driver is not found.')
except RuntimeError:
    print('Driver fails to initialize.')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def print_speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def speech(text):
    from gtts import gTTS
    import pygame
    import io
    speech = gTTS(text=text, lang='hi', slow=False)
    audio_fp = io.BytesIO()
    speech.write_to_fp(audio_fp)
    audio_fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_fp, 'mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
