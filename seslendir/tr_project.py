from gtts import gTTS

def seslendir(text):
    tts = gTTS(text, lang='tr')
    tts.save("seslendirme.mp3")
    

if __name__ == '__main__':
    metin = input("Seslendirmek istediğiniz metni girin: ")
    seslendir(metin)
