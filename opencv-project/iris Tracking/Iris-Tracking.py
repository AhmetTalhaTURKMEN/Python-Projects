import cv2

# Kamera ayarları
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Cascade sınıflandırıcısı yükleme
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
    # Kameradan görüntü al
    ret, frame = cap.read()

    # Görüntüyü griye çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gözleri tespit et
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Gözlerin merkez noktasını hesapla
    if len(eyes) > 0:
        eye_center = (int(eyes[0][0] + eyes[0][2]/2),
                      int(eyes[0][1] + eyes[0][3]/2))
    else:
        eye_center = None

    # Çizgiyi çiz
    if eye_center is not None:
        screen_center = (320, 240) # Ekran merkezi koordinatları
        x_diff = eye_center[0] - screen_center[0]
        y_diff = eye_center[1] - screen_center[1]
        endpoint = (eye_center[0] + x_diff, eye_center[1] + y_diff)
        cv2.line(frame, eye_center, endpoint, (0, 0, 255), 2)

    #    if eye_center is not None:
    #     screen_center = (320, 240) # Ekran merkezi koordinatları
    #     x_diff = eye_center[0] - screen_center[0]
    #     y_diff = eye_center[1] - screen_center[1]
    #     endpoint = (eye_center[0] + x_diff, eye_center[1] + y_diff)
    #     cv2.line(frame, eye_center, endpoint, (0, 0, 255), 2)


    # Görüntüyü göster
    cv2.imshow('frame', frame)

    # Çıkış için q tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Belleği serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
