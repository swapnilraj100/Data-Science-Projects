import os
import cv2
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import Sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# Directory structure
base_dir = r"D:\VS_PYTHON\ML\pedestrian_dataset"
raw_images_dir = os.path.join(base_dir, "PNGImages")
resized_images_dir = os.path.join(base_dir, "Resized_Images")
json_output_path = os.path.join(base_dir, "manual_pedestrian_bboxes_New.json")

# Make sure the resized image folder exists
os.makedirs(resized_images_dir, exist_ok=True)

# Image dimensions
original_dim = (512, 512)
target_dim = (224, 224)
batch_size = 2

# HOG-based pedestrian detector
hog_detector = cv2.HOGDescriptor()
hog_detector.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def extract_pedestrian_boxes(img):
    resized_img = cv2.resize(img, original_dim)
    detected, _ = hog_detector.detectMultiScale(resized_img, winStride=(4, 4), padding=(8, 8), scale=1.05)
    return [{"x": int(x), "y": int(y), "width": int(w), "height": int(h)} for (x, y, w, h) in detected]

# Generate bounding boxes and save resized images
all_bboxes = {}
for fname in os.listdir(raw_images_dir):
    if fname.lower().endswith((".png", ".jpg", ".jpeg")):
        full_path = os.path.join(raw_images_dir, fname)
        img = cv2.imread(full_path)
        if img is None:
            continue
        img_resized = cv2.resize(img, original_dim)
        cv2.imwrite(os.path.join(resized_images_dir, fname), img_resized)
        detected_boxes = extract_pedestrian_boxes(img_resized)
        all_bboxes[fname] = detected_boxes

# Save detections to a JSON file
with open(json_output_path, "w") as f:
    json.dump(all_bboxes, f, indent=4)

# Reload bounding box data
with open(json_output_path, "r") as f:
    all_bboxes = json.load(f)

# Custom data generator for training
class PedestrianDataGenerator(Sequence):
    def __init__(self, filenames, annotations, batch_sz):
        self.filenames = filenames
        self.annotations = annotations
        self.batch_sz = batch_sz

    def __len__(self):
        return int(np.ceil(len(self.filenames) / self.batch_sz))

    def __getitem__(self, idx):
        batch_imgs = self.filenames[idx * self.batch_sz : (idx + 1) * self.batch_sz]
        batch_annots = self.annotations[idx * self.batch_sz : (idx + 1) * self.batch_sz]

        X, y = [], []
        for i, fname in enumerate(batch_imgs):
            img_path = os.path.join(resized_images_dir, fname)
            img = cv2.imread(img_path)
            if img is None:
                continue
            img = cv2.resize(img, target_dim) / 255.0
            boxes = batch_annots[i]
            padded = boxes[:2] if len(boxes) >= 2 else boxes + ([{"x": 0, "y": 0, "width": 0, "height": 0}] * (2 - len(boxes)))

            label = []
            for box in padded:
                label += [
                    box["x"] / original_dim[0],
                    box["y"] / original_dim[1],
                    box["width"] / original_dim[0],
                    box["height"] / original_dim[1]
                ]

            X.append(img)
            y.append(label)

        if not X:
            return np.zeros((self.batch_sz, 224, 224, 3)), np.zeros((self.batch_sz, 8))

        return np.array(X), np.array(y)

# Prepare the data
image_files = list(all_bboxes.keys())
label_data = [all_bboxes[fname] for fname in image_files]
data_gen = PedestrianDataGenerator(image_files, label_data, batch_size)

# Define a basic CNN model
model = Sequential([
    Input(shape=(224, 224, 3)),
    Conv2D(16, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(8, activation='sigmoid')
])

# Compile and train the model
model.compile(optimizer=Adam(learning_rate=0.001), loss="mse", metrics=["mae"])
model.fit(data_gen, epochs=10)
model.save("pedestrian_detector.h5")

print("Training complete! Model saved as pedestrian_detector.h5")

# Visual evaluation on test samples
for idx in range(min(3, len(image_files))):
    file = image_files[idx]
    path = os.path.join(resized_images_dir, file)
    img = cv2.imread(path)
    img_input = cv2.resize(img, target_dim) / 255.0

    pred = model.predict(np.expand_dims(img_input, axis=0))[0]

    # Predicted boxes (green)
    for i in range(2):
        px = int(pred[i*4 + 0] * original_dim[0])
        py = int(pred[i*4 + 1] * original_dim[1])
        pw = int(pred[i*4 + 2] * original_dim[0])
        ph = int(pred[i*4 + 3] * original_dim[1])
        cv2.rectangle(img, (px, py), (px + pw, py + ph), (0, 255, 0), 2)

    # Actual boxes (blue)
    for box in all_bboxes[file]:
        ax, ay, aw, ah = int(box["x"]), int(box["y"]), int(box["width"]), int(box["height"])
        cv2.rectangle(img, (ax, ay), (ax + aw, ay + ah), (255, 0, 0), 2)

    plt.figure()
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(f"{file} — Predicted (Green) vs Actual (Blue)")
    plt.axis("off")
    plt.show()
