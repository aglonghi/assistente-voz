import os
import datetime
import RPi.GPIO as GPIO

LED = 25
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

def falar(mensagem):
    os.system(f'espeak-ng -v pt "{mensagem}"')

def executar(comando):
    if "hora" in comando:
        agora = datetime.datetime.now().strftime("%H:%M")
        falar(f"Agora são {agora}")
    elif "ligue a luz" in comando:
        GPIO.output(LED, GPIO.HIGH)
        falar("Luz ligada")
    elif "desligue a luz" in comando:
        GPIO.output(LED, GPIO.LOW)
        falar("Luz desligada")
    elif "curiosidade" in comando:
        falar("Você sabia que o polvo tem três corações?")
    else:
        falar("Desculpe, não entendi o comando.")
