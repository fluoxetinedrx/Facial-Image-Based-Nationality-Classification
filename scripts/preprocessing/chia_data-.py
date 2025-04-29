import os

folder_path = r"F:\study\project\Facial-Image-Based-Nationality-Classification\datasets\dataset\test"
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

image_count = 0

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.lower().endswith(image_extensions):
            image_count += 1

print(f"Tổng số ảnh: {image_count}")