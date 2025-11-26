import os
import speech_recognition as sr
import random

def tebakan():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nSilakan ucapkan jawabannya...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    return r.recognize_google(audio, language="en-EN").lower()

def permainan():
    words = {"permainan" : "game", "komputer" : "computer", "teknologi" : "technology"}
    indonesian, english = random.choice(list(words.items()))

    print(f'\nSebutkan "{indonesian}" dalam bahasa Inggris!')
    
    try:
        kata = tebakan()
        if kata == english:
            print("Benar!")
        else:
            print(f"Salah. Jawaban: {english}")

    except:
        print("Tidak bisa mengenali suara.")
permainan()