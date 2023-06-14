import cv2

# Gözlerin algılanması için cascade sınıflandırıcıyı yükleme
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Yüz algılaması için cascade sınıflandırıcısını yükleme
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Kamera sinyalini yakalamak için VideoCapture nesnesi oluşturma
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir görüntü al
    ret, frame = cap.read()

    # Görüntü griye dönüştürülür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüz tespiti için cascade sınıflandırıcısını kullan
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Yüzün olduğu koordinatları kullanarak mavi dikdörtgen çizme
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Gözlerin tespiti için cascade sınıflandırıcısını kullan
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Gözlerin olduğu koordinatları kullanarak yeşil dikdörtgen çizme
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Sonuç görüntüyü gösterme
    cv2.imshow('frame', frame)

    # Eğer 'q' tuşuna basılırsa döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Belleği temizleme
cap.release()
cv2.destroyAllWindows()
