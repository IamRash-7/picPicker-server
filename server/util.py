import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
import cv2
import base64

IMAGE_SHAPE = (224, 224)
reconstructed_model = keras.models.load_model("../my_model")
image_labels = []
with open("./ImageNetLabels.txt", "r") as f:
    image_labels = f.read().splitlines()

def get_cv2_image_from_base64_string(b64str):
    encoded_data = b64str.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def classify_image(image_base64_data=None, file_path=None):
    if file_path:
        img = cv2.imread(file_path)
    else:
        img = get_cv2_image_from_base64_string(image_base64_data)
    img = cv2.resize(img, IMAGE_SHAPE)
    img = np.array(img)/255.0
    result = reconstructed_model.predict(img[np.newaxis, ...])
    predicted_label_index = np.argmax(result)
    return image_labels[predicted_label_index]


# classify_image(file_path="C:/Users/bbabi/Desktop/download (1).jfif")