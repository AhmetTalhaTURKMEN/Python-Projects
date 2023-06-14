import pyttsx3

def seslendir(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Ses hızı ayarı (varsayılan: 200)
    engine.setProperty('volume', 0.7)  # Ses şiddeti ayarı (varsayılan: 1.0)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    metin = input("Seslendirmek istediğiniz metni girin: ")
    seslendir(metin)
