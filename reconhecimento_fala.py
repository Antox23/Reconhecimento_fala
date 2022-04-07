from cgitb import text
#importando a biblioteca de reconhecimento de voz e, tambem instalar o pyaudio.
import speech_recognition as sr

#reconhecer audio
rec = sr.Recognizer()

#microfone vira mic
with sr.Microphone() as mic:
    #ajustar ruídos do mic
    rec.adjust_for_ambient_noise(mic)
    print("Testando fala!")
    #audio receber rec.listen para ouvir, ou seja, o programa vai ouvir a voz do mic
    audio = rec.listen(mic)
    #texto vai receber a biblioteca de audio da google, e traduzo a voz pra br
    texto = rec.recognize_google(audio, language='pt-BR')
    #printando texto
    print(texto)