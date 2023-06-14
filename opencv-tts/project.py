import cv2
import pyttsx3
import threading

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Cascade sınıflandırıcısını yükleme
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamera yakalayıcısını başlatma
cap = cv2.VideoCapture(0)

# Seslendirme motorunu başlatma
engine = pyttsx3.init()

while True:
    # Kameradan bir çerçeve alınması
    ret, frame = cap.read()

    # Çerçeveyi gri tona dönüştürme
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüz tespiti yapma
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Yüzlerin etrafına dikdörtgen çizme ve "Biri girdi" deme
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Seslendirme işlemini ayrı bir iş parçacığında gerçekleştirme
        threading.Thread(target=speak, args=("Biri girdi",)).start()

    # Sonuçları gösterme
    cv2.imshow('Camera', frame)

    # Çıkış için 'q' tuşuna basma kontrolü
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kapatma işlemleri
cap.release()
cv2.destroyAllWindows()
engine.stop()
