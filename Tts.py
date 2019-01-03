from gtts import gTTS
import os


def read_text(text_param):
    tts = gTTS(text=text_param,lang='en')
    tts.save("goodtest.mp3")
    os.system('goodtest.mp3')