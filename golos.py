


import pyaudio
import audioop
import datetime

from gtts import gTTS   # речь из текста
import os
import time

import winsound

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 1200

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK,
                       exception_on_overflow=False)
    rms = audioop.rms(data, 2)
    #decibel = 20 * math.log10(rms)
    print(rms)

    def zzz():
        print("ПРИВЫШЕН УРОВЕНЬ ЗВУКА")
        now = datetime.datetime.now()
        now


        print(now.strftime("%I:%M:%S:%f")) #часы, минуты, секунды и милисек.

        aaa = now - datetime.datetime.now() #вычитание времени
        print(aaa)


        datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
        print(now)

    if rms>1000:   # предел звука
        zzz()

        #winsound.PlaySound("SystemExit", winsound.SND_ALIAS)  # системный звук
        #winsound.PlaySound("*", winsound.SND_ALIAS)

        mytext = "заткнись пожалуйста"
        audio = gTTS(text=mytext, lang="ru", slow=False)  # en
        #audio.save("example3.mp3")    # сохранять один раз
        os.system("start example3.mp3")

        time.sleep(5)

    print(rms)

stream.stop_stream()
stream.close()
p.terminate()