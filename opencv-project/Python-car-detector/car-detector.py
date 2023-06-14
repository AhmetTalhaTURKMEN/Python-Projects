import cv2

# Kamera kaynağı olarak varsayılan kamerayı kullanın.
cap = cv2.VideoCapture(0)

# Araba tanıma için eğitilmiş bir sınıflandırıcı yükleyin.
car_cascade = cv2.CascadeClassifier('car_classifier.xml')

while True:
    # Kamera kaynağından bir kare alın.
    ret, frame = cap.read()

    # Gri tonlamalı görüntü elde edin.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Araba sınıflandırıcısı kullanarak arabaları tespit edin.
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Tespit edilen her arabayı dikdörtgen kutularla işaretleyin.
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Sonuç görüntüsünü gösterin.
    cv2.imshow('Car Detection', frame)

    # 'q' tuşuna basarak çıkış yapın.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırakın ve pencereyi kapatın.
cap.release()
cv2.destroyAllWindows()
