import os
import json
import time
import RPi.GPIO as GPIO
import pyaudio
from vosk import Model, KaldiRecognizer
from comandos.acoes import executar

BOTAO = 23
LED = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(BOTAO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

modelo = Model("modelos/vosk-model-small-pt-0.3")
rec = KaldiRecognizer(modelo, 16000)
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def ouvir_comando():
    print("Aguardando fala...")
    GPIO.output(LED, GPIO.HIGH)
    texto = ""
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            resultado = json.loads(rec.Result())
            texto = resultado.get("text", "")
            break
    GPIO.output(LED, GPIO.LOW)
    print(f"Comando reconhecido: {texto}")
    return texto

try:
    print("Sistema pronto. Pressione o botão para falar.")
    while True:
        if GPIO.input(BOTAO) == GPIO.LOW:
            comando = ouvir_comando()
            if comando:
                executar(comando)
            time.sleep(0.5)
except KeyboardInterrupt:
    print("Encerrando assistente.")
finally:
    GPIO.cleanup()
    stream.stop_stream()
    stream.close()
    audio.terminate()
