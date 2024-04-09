import os
import cv2
import time
import uuid

number_of_classes = 1  #Number of words/phrases to train
images_per_class = 10  #Number of images per class
esp32_url = 'http://192.168.12.24:81/stream'  #IP of the ESP32 camera

RAW_IMAGES_DIR = 'RAW'

for j in range(number_of_classes):
    class_folder = os.path.join(RAW_IMAGES_DIR, f"Class_{j}")
    if not os.path.exists(class_folder):
        os.makedirs(class_folder)

    #Attempt to access the video stream
    cap = cv2.VideoCapture(esp32_url)
    if not cap.isOpened():
        print(f"Error: Could not open video stream from class {j}.")
        continue

    print(f'Starting data collection for class {j}')

    number = 0
    start_time = time.time()

    while number < images_per_class:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            continue
        
        #Display the frame in a window
        cv2.imshow(f"Class_{j} Frame", frame)
        cv2.waitKey(1)

        #Check if 5 seconds have passed since the last photo
        if time.time() - start_time >= 5:
            # Save the captured frame to disk
            image_name = f"{uuid.uuid4()}.jpg"
            cv2.imwrite(os.path.join(class_folder, image_name), frame)
            print(f"Image {number} captured.")
            number += 1
            start_time = time.time()

cap.release()
cv2.destroyAllWindows()
print("Data collection complete.")
