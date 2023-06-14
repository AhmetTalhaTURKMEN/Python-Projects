import cv2
import tensorflow as tf

# Yüz tanıma modeli için CascadeClassifier yükleniyor
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Yaş tahmin modeli için eğitilmiş bir TensorFlow modeli yükleniyor
age_model = tf.keras.models.load_model('age_model.h5')

# Kişi resmini yüzleri bulmak için işleyen ve yaş tahmini yapabilen bir fonksiyon
def predict_age(image_path):
    # Resmi oku
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Yüzleri bul
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Her bir yüz için yaş tahmini yap
    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]
        resized_img = cv2.resize(face_img, (224, 224))
        normalized_img = resized_img / 255.0
        reshaped_img = normalized_img.reshape((1, 224, 224, 1))
        result = age_model.predict(reshaped_img)
        age = int(result[0][0])
        
        # Sonucu yazdır
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, f'Age: {age}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Tahmin sonuçlarını göster
    cv2.imshow('Age Prediction', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Kişi resmi dosya yolunu belirtin ve yaş tahmini yapın
image_path = 'resim.jpeg'
predict_age(image_path)
