import cv2
import os
import shutil

# Load bộ cascade phát hiện khuôn mặt của OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Đường dẫn dữ liệu
input_dir = 'datasets/raw/test_images_data'
clean_dir = 'datasets/processed/test_cleaned_images'
no_face_dir = 'datasets/processed/test_no_face_images'

# Tạo thư mục lưu kết quả
os.makedirs(clean_dir, exist_ok=True)
os.makedirs(no_face_dir, exist_ok=True)

# Duyệt qua từng người
for person_name in os.listdir(input_dir):
    person_path = os.path.join(input_dir, person_name)

    clean_person_path = os.path.join(clean_dir, person_name)
    no_face_person_path = os.path.join(no_face_dir, person_name)
    os.makedirs(clean_person_path, exist_ok=True)
    os.makedirs(no_face_person_path, exist_ok=True)

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        try:
            img = cv2.imread(img_path)
            if img is None:
                raise ValueError("Không đọc được ảnh.")

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3, minSize=(30, 30))

            if len(faces) == 0:
                shutil.copy(img_path, os.path.join(no_face_person_path, img_name))
                print(f"[❌] NO FACE: {img_name}")
            else:
                shutil.copy(img_path, os.path.join(clean_person_path, img_name))
                print(f"[✅] HAS FACE: {img_name}")
        except Exception as e:
            print(f"[⚠️] Lỗi xử lý {img_name}: {e}")